import os
from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('SQLALCHEMY_DATABASE_URI'))
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('TEST_DB_URI'))
from application import routes