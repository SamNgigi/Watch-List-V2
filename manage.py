#!/usr/bin/env python
# We add the db import from our app
from app import create_app, db
# We import the User class, Role class
from app.models import User, Role
from flask_script import Manager, Server
""" 
Using flask-migrate we are able to use alembic. 

This is a tool that automatically create and tracks DATABASE
MIGRATIONS from changes to our SQL models.

DATABASE MIGRATIONS are records of all the changes of our database
schema.

Alembic allows us to upgrade or downgrade our database to saved
versions
"""
from flask_migrate import Migrate, MigrateCommand

# Instanciating our app through our create app function.
app = create_app('development')

# Instanciating serving functionality
manager = Manager(app)
manager.add_command('server', Server)
# Instanciating db migration functionality.
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

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