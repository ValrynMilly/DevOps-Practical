from flask import Flask, url_for, render_template, redirect, request

from application.forms import namegen
import requests
import string
import random

app = Flask(__name__)
servicetwo = 'http://localhost:5001'
servicethree = 'http://localhost:5002'
servicefour = 'http://localhost:5003'
app.config['SECRET_KEY']='Thisissecret'

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


if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000, debug=True)