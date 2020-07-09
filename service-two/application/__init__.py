from flask import Flask
from os import getenv
app = Flask(__name__)
app.config['SECRET_KEY']='Thisisanothersecret'
from application import routes