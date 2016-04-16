"""
jobnownow_website
~~~~~~~~~~~~~~~~~

Preclaunch website for collecting subscription emails
for when the JobNowNow app launches.

:author: Krohx Technologies (krohxinc@gmail.com)
:copyright: (c) 2016 by Krohx Technologies
:license: see LICENSE for details.
"""

# standard lib imports
import os

# library imports
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask import redirect, request

# local imports
from config import Config, DevConfig

#export JOBNOWNOW_EMAIL_CFG=dev
app = Flask(__name__)
cfg = os.getenv('JOBNOWNOW_EMAIL_CFG') 

if cfg is None or cfg != 'dev':
    app.config.from_object(Config)
else:
    app.config.from_object(DevConfig)

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





# from flask_slack import Slack

# subs = db_ops.ret_all(db_ops.Subscription)
# emails = [sub.email for sub in subs]

# slack = Slack(app)



# @slack.command('bot_test', token=app.config['SLACK_TOKEN'], methods=['POST'])
# def action(**kwargs):
#     text = kwargs.get('text')
#     return slack.response('New subscriber: %r' %)

# app.add_url_rule('/subscribe/', view_func=slack.dispatch)



