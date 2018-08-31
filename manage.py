#!/usr/bin/env python
# We add the db import from our app
from app import create_app, db
# We import the User class, Role class
from app.models import User, Role
from flask_script import Manager, Server

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

""" 
We use the @manage.shell decorator to create a shell context and the
make_shell_context function allows us to pass in some properties into
our shell.

We return the app instance, the db instance and the User class thus allowing our app models to communicate with db via shell.

To run the shell we use python manage.py shell.
"""
@manager.shell
def make_shell_context():
  return dict(app=app, db=db, User=User, Role=Role)


if __name__ == '__main__':
  manager.run()