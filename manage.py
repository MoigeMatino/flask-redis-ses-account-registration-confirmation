# manage.py

import redis
import sys
import unittest

from flask.cli import FlaskGroup

from project.server import create_app, db
from project.server.models import User
from rq import Connection, Worker


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('create_db')
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('drop_db')
def drop_db():
    """Drops the db tables."""
    db.drop_all()


@cli.command('test')
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        sys.exit(0)
    else:
        sys.exit(1)

@cli.command('run_worker')
def run_worker():
    redis_url = app.config['REDIS_URL']
    redis_connection = redis.from_url(redis_url)
    with Connection(redis_connection):
        worker = Worker(app.config['QUEUES'])
        worker.work()



if __name__ == '__main__':
    cli()
