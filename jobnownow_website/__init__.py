"""
jobnownow_website
~~~~~~~~~~~~~~~~~

Preclaunch website for collecting subscription emails
for when the JobNowNow app launches.

:author: Krohx Technologies (krohxinc@gmail.com)
:copyright: (c) 2016 by Krohx Technologies
:license: see LICENSE for details.
"""

# library imports
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask import redirect, request

# local imports
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.config['DEBUG'] = False

# Instantiate Flask extensions
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

import db_ops # to avoid issue around circular imports

REDIRECT_URL = 'http://jobnownow.com/thankyou.html'


@app.route('/index/')
@app.route('/')
def index():
    return redirect(REDIRECT_URL)


@app.route('/subscribe/<email>/')
def subscribe(email=''):
    
    if validate_email(email):
        db_ops.insert_val(db_ops.Subscription, dict(email=email))
        print "Registered!"
    else:
        db_ops.insert_val(db_ops.InvalidSub, dict(email=email))
        print "Failed!"

    return redirect(REDIRECT_URL)

    
@app.route('/subscribe/', methods=['GET', 'POST'])
def subscribe_form():
    form = request.form
    email = form['email'].decode('utf-8')

    if validate_email(email):
        db_ops.insert_val(db_ops.Subscription, dict(email=email))
        print "Registered!"
    else:
        db_ops.insert_val(db_ops.InvalidSub, dict(email=email))
        print "Failed!"

    return redirect(REDIRECT_URL)


# `validate_email` snippet from online
def validate_email(email):
    sep=[x for x in email if not x.isalpha()]
    sepjoined=''.join(sep)
    ## sep joined must be ..@.... form
    if sepjoined.strip('.') != '@': return False
    end=email
    for i in sep:
        part,i,end=end.partition(i)
        if len(part)<2: return False
    return True



if __name__ == '__main__':
    db.create_all()
    app.run()