from flask import Flask, url_for, render_template, redirect, request
from forms import namegen
import string
import random
import requests

app = Flask(__name__)
serviceone = 'http://localhost:5000'
app.config['SECRET_KEY']='Thisissecret'

@app.route('/')
def namegenform_post():
    orcnames = ['uk', 'guk', 'keg', 'rag', 'kha', 'rok', 'zok', 'huk', 'rik']
    #orc names will be their own route soon
    elvnames = ['iros', 'ilir', 'tris', 'aren', 'ana', 'ina', 'enys', 'ona', 'dir']
    requestfirst = requests.get(serviceone, params=first_name)
    requestlast = requests.get(serviceone, params=last_name)
    genfirst = requestfirst[:2]
    gensecond = requestlast[:3]
    username = (random.choice(elvnames) + genfirst + gensecond + random.choice(elvnames)) 
    return username.upper()


if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5001, debug=True)