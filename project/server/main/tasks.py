import time
import boto3
import os

from project.server import db
from project.server.models import User


def send_email(email, body):
    ses = boto3.client(
        'ses',
        region_name=os.environ.get('SES_REGION'),
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
    )
    ses.send_email(
        Source=os.environ.get('SES_EMAIL_SOURCE'),
        Destination={
            'ToAddresses': [email]
        },
        Message={
            'Subject': 
                {'Data': 'Confirm Your Account'},
            'Body': {
                'Text': {'Data': body}
            }
        }
    )
    user = User.query.filter_by(email=email).first()
    user.email_sent = True
    db.session.commit()
    return True
