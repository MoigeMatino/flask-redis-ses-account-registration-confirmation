import time

from project.server import db
from project.server.models import User


def send_email(email):
    # TODO: replace with actual sending email functionality
    time.sleep(10) # simulate a process that takes time
    user = User.query.filter_by(email=email).first()
    user.email_sent = True
    db.session.commit()
    return True
