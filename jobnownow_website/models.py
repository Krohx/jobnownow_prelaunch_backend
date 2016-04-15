"""
jobnownow_website.models
~~~~~~~~~~~~~~~~~~~~~~~~

A package for different database ORM models.

:author: Krohx Technologies (krohxinc@gmail.com)
:copyright: (c) 2016 by Krohx Technologies
:license: see LICENSE for details.
"""

# standard library imports
from datetime import datetime

# local imports
from jobnownow_website import db


class Subscription(db.Model):

    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, default='no_email', nullable=True, unique=False)
    datetime = db.Column(db.String, default=datetime.utcnow, unique=False)


class InvalidSub(db.Model):

    __tablename__ = 'invalid_subs'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, default='no_email', nullable=True, unique=False)
    datetime = db.Column(db.String, default=datetime.utcnow, unique=False)