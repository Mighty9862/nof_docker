# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = '1d44b186ad979a5c359f11ca'
db = SQLAlchemy(app)
manager = LoginManager(app)


from nucleus import models, routes, errors
from nucleus.plugins import login, admin
from nucleus.user import profile
from nucleus.plugins.test import create_data_from_bd


with app.app_context():
        db.create_all()
        create_data_from_bd()

