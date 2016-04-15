"""
jobnownow_website.db_ops
~~~~~~~~~~~~~~~~~~~~~~~~

Database ORM Utilities.

Bunch of Utility functions for doing CRUD over ORM.

:author: Krohx Technologies (krohxinc@gmail.com)
:copyright: (c) 2016 by Krohx Technologies
:license: see LICENSE for details.
"""

from jobnownow_website.models import *

#db.create_all()


# insert given record into specified table(model)
def insert_val(model, param_dict):
	"""
	Inserts values of fields present in `param_dict` into a new row of
	the table `model` of the database.
	"""
	row = model(**param_dict)
	db.session.add(row)
	commit_db()


# insert given list of values into specified table (model)
def insert_vals(model, dict_list):
	"""
	Inserts values of fields present in each dict of `dict_list` into 
	new rows accordingly in the table `model` of the database.
	"""
	for param_dict in dict_list:
		insert_val(model, param_dict)


# update database with data
# :param: `model` DB table to be updated
# :param: `param_dict_ret` dict holding keyword args with which to
# retrieve previous data, before updation
# :param: `param_dict_ins` dict holding keyword args with which to
# insert new data
def update_row(model, param_dict_ret, param_dict_ins):
	row = model.query.filter_by(**param_dict_ret).update(param_dict_ins)
	commit_db()


# Retreive record from specified table (model) using given key (for
# field) and value (as record)
def ret_val(model, param_dict):
	row = model.query.filter_by(**param_dict).first()
	return row


# Retreive records from specified table (model) using given key (for
# field) and value (as record)
def ret_all_val(model, param_dict):
	row = model.query.filter_by(**param_dict).all()
	return row


# Retreive all records from specified table (model)
def ret_all(model):
	rows = model.query.all()
	return rows


# commit changes to the database
def commit_db():
	db.session.commit()


def get_obj(model, obj):
	ret_val
