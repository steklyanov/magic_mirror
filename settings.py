from flask import Flask
from flask_restful import Api
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, Manager, MigrateCommand

app = Flask(__name__)

# API SETTINGS
api = Api(app)
# DATABASE SETTINGS
basedir = os.path.abspath(os.path.dirname(__file__))  # resolve current directory path
# create database in the root of the project
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Migrate database
migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)
# init marshmallow for data serialization
ma = Marshmallow(app)
