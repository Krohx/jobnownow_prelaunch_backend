"""
config
~~~~~~

Application configuration module.

:author: Krohx Technologies (krohxinc@gmail.com)
:copyright: (c) 2016 by Krohx Technologies
:license: see LICENSE for details.
"""

# standard library imports
import os

"""
Global variables
"""
# This will get the absolute path to the module that
# imports this config file using the '__file__'
# attribute.
BASE_URI = os.path.dirname(__file__)

# Get absolute path to user's home directory                
HOME_DIR = os.path.expanduser('~/')                 # '/' is added to ensure the path has a trailing slash

# Let's store the name of the application
# package here. This is recommended to be
# the value of the `import_name` argument
# when creating the `Flask` application object.
APP_NAME = 'jobnownow_website'


"""
Configuration classes.

Class `Config` class is the base/super class.

`DevConfig`, `TestingConfig` and `ProductionConfig` all extend the base
class: `Config`
"""
class Config():
    """
    Base configuration class. Has all the common configuration
    properties.
    """
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('CSRF_SESSION_SECRET_KEY') or \
        'ns984hoa0hfa908hw4fa045gf0angvajwfvpafzsdjnafpw4gtandgfvawtngarginf'
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT') or \
        'vpafpw4gfzsrginf908hw4dj043henf0h03nwtngafa045gfangvajwaa0vaftandgf'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    THREADS_PER_PAGE = 2    
    APP_NAME = APP_NAME
    DB_URI = os.path.join(BASE_URI, '.jobnownow_website_data.sqlite')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_URI
    APP_STATIC_DATA_URI = os.path.join(BASE_URI, APP_NAME, 'data')

    # email specifics
    MAIL_DEFAULT_SENDER = 'pythonflask@yahoo.com'
    MAIL_SERVER = 'smtp.mail.yahoo.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # gmail authentication
    MAIL_USERNAME = os.environ.get('APP_MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('APP_MAIL_PASSWORD')

    @staticmethod
    def init_app(app, *args):
        """
        Method to initialize instances of Flask extensions passed in as
        a list of parameters.
        """
        for flask_extension in args:
            flask_extension.init_app(app)

