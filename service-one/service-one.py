from flask import Flask, url_for, render_template, redirect, request
from forms import namegen
import requests
import string
import random

app = Flask(__name__)
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
        name = requests.get(servicetwo)
        title = requests.get(servicethree)
        data = [name.text, title.text]
        result = requests.post(servicefour, data)
        return result.text


if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000, debug=True)
