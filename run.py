#!/usr/bin/env python
"""
run
~~~

Module to run the whole application

:author: Krohx Technologies (krohxinc@gmail.com)
:copyright: (c) 2016 by Krohx Technologies
:license: see LICENSE for details.
"""

# standard library imports
import os

# library imports
from flask.ext.script import Manager, Shell, Command

# local imports
from jobnownow_website import app, db

# Create `Manager` instance for Flask extension "Flask-script"
app_manager = Manager(app)
db.create_all()


# Callback function that'll be used for passing objects that we might
# need, to test/run the application within the context of a shell
def make_shell_context():
    return dict(app=app, db=db, db_ops=db_ops)

# Add commands to shell context
app_manager.add_command('shell', Shell(make_context=make_shell_context))


# Run the application
if __name__ == '__main__':
    app_manager.run()
