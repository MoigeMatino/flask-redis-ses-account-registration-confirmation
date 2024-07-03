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


main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/', methods=['GET', 'POST'])
def home():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                user = User(email=form.email.data)
                db.session.add(user)
                db.session.commit()
                redis_url = current_app.config['REDIS_URL']
                # connect to redis
                with Connection(redis.from_url(redis_url)):
                    # create a new Queue instance
                    q = Queue()
                    # enqueue task to be executed
                    q.enqueue(send_email, user.email)
                flash('Thank you for registering.', 'success')
                return redirect(url_for("main.home"))
            except IntegrityError:
                db.session.rollback()
                flash('Sorry. That email already exists.', 'danger')
    users = User.query.all()
    return render_template('home.html', form=form, users=users)
