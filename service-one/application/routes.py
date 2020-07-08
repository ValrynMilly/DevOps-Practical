from flask import Flask, url_for, render_template, redirect, request
from application import app
from application.forms import namegen
import requests
import string
import random

servicetwo = 'http://localhost:5001'
servicethree = 'http://localhost:5002'
servicefour = 'http://localhost:5003'


@app.route('/')
def namegenform():
    form = namegen(request.form)
    return render_template('namegen.html', title='namegen', form=form)

@app.route('/', methods=['POST'])
def namegenform_post():
    form = namegen()
    if form.is_submitted():
        name = requests.get(servicetwo)
        return name.upper()