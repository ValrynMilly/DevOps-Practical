from flask import Flask, url_for, render_template, redirect, request, Response
from application import app, db
from application.forms import namegen
from os import getenv
from application.models import Registerfantasy
import requests
import string
import random

servicetwo = 'http://service-two:5001'
servicethree = 'http://service-three:5002'
servicefour = 'http://service-four:5003'

app.config['SECRET_KEY'] = getenv("SECRET_KEY")

@app.route('/')
def namegenform():
    form = namegen(request.form)
    return render_template('namegen.html', title='namegen', form=form)

@app.route('/', methods = ['POST'])
def namegenform_post():
    form = namegen()
    if form.validate_on_submit():
        name = requests.get(servicetwo)
        title = requests.get(servicethree)
        result = requests.get(servicefour)
        fresh_register = Registerfantasy(fan_name=name.text, fan_title=title.text, fan_story=result.text)
        db.session.add(fresh_register)
        db.session.commit()
        return result.text