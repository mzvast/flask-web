import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__,instance_relative_config=True)

app.config.from_object('config.default')

app.config.from_pyfile('config.py')

# app.config.from_envvar('APP_CONFIG_FILE')

db = SQLAlchemy(app)

from .views import home
from .views.profile import profile
from . import models

# bluePrint register
# app.register_blueprint(profile,url_prefix='/<user_url_slug>')

