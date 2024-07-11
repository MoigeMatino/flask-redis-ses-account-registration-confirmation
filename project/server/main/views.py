# project/server/main/views.py

import redis
from flask import render_template, Blueprint, url_for, \
    redirect, flash, request, current_app
from rq import Queue, Connection
from sqlalchemy.exc import IntegrityError

from project.server import db
from project.server.models import User
from project.server.main.forms import RegisterForm
from project.server.main.tasks import send_email
from project.server.main.utils import encode_token, generate_url, decode_token


main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/', methods=['GET', 'POST'])
def home():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                user = User(email=form.email.data)
                # save user to db
                db.session.add(user)
                db.session.commit()
                # generate token, confirm url and template
                token = encode_token(user.email)
                confirm_url = generate_url('main.confirm_email', token)
                body = render_template('email.txt', confirm_url=confirm_url)
                redis_url = current_app.config['REDIS_URL']
                # connect to redis
                with Connection(redis.from_url(redis_url)):
                    # create a new Queue instance
                    q = Queue()
                    # enqueue task to be executed
                    q.enqueue(send_email, user.email, body)
                flash('Thank you for registering.', 'success')
                flash('Please check your email to confirm your account.', 'success')
                return redirect(url_for("main.home"))
            except IntegrityError:
                db.session.rollback()
                flash('Sorry. That email already exists.', 'danger')
    users = User.query.all()
    return render_template('home.html', form=form, users=users)

@main_blueprint.route('/confirm/<token>')
def confirm_email(token):
    decoded_email = decode_token(token)
    if not decoded_email:
        flash('The confirmation link is invalid.Please request a new one.', 'danger')
        redirect(url_for('main.home'))
    elif decoded_email == "Token expired":
        flash('The confirmation link has expired. Please request a new one.', 'warning')
        redirect(url_for('main.home'))
    elif decoded_email == "Invalid token signature":
        flash('The confirmation link is invalid. Please try again.', 'danger')
    user = User.query.filter_by(email=decoded_email).first()
    #ccheck if user is already confirmed
    if user.confirmed:
        flash('User already confirmed.', 'success')
        return redirect(url_for('main.home'))
    # confirm user and save status to db
    user.confirmed = True
    db.session.add(user)
    db.commit()
    flash('Your email has been successfully confirmed!', 'success')
    return redirect(url_for('main.home'))

