#!/usr/bin/env python
# We add the db import from our app
from app import create_app, db
# We import the User class, Role class
from app.models import User, Role
from flask_script import Manager, Server
# We add flask_migrate that will allow us to update the schema
from flask_migrate import Migrate, MigrateCommand

# Instanciating our app through our create app function.
app = create_app('development')

# Instanciating serving functionality
manager = Manager(app)
manager.add_command('server', Server)
# Instanciating db migration functionality.
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
  """ Running unit tests """
  import unittest
  test = unittest.TestLoader().discover("tests")
  unittest.TextTestRunner(verbosity=2).run(tests)

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