from flask import Flask, url_for, render_template, redirect, request, Response
from application import app
from application.forms import namegen
from application.models import Registerfantasy
import requests
import string
import random

servicetwo = 'http://service-two:5001'
servicethree = 'http://service-three:5002'
servicefour = 'http://service-four:5003'

app.config['SECRET_KEY']='Thisisanothersupersupersupersecret'

@app.route('/')
def namegenform():
    form = namegen(request.form)
    return render_template('namegen.html', title='namegen', form=form)

@app.route('/', methods = ['POST'])
def namegenform_post():
    form = namegen()
    if form.validate_on_submit():
        story = requests.get(servicefour)
        result = requests.post(servicefour, story.text)
        return result.text