import random
import string
import sys
import requests

from flask import Flask, url_for, render_template, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY']='Thisisanothersuperdupersecret'

@app.route('/', methods=['GET'])
def titlegen_post():
    where = ['In a bar','On a field', 'Through the clouds', 'Under a mountain', 'Underwater', 'In a town']
    action = ['killed', 'annihilated', 'destroyed', 'Poisoned', 'Petrified', 'Saved', 'Rescued', 'Healed', 'Silenced']
    instrument = ['a pinkie', 'a pencil', 'a hammer', 'a bow', 'lightning', 'fire', 'a hunt'] 
    shortstory = (random.choice(where) + " " + "USERNAME" + " " + "title" +" Once " + random.choice(action)+ " " + str(random.randint(1, 3000)) + " MEN WITH " + random.choice(instrument)) 
    #so USERNAME & TITLE will be post request sent from service one which will be read then generated
    return shortstory.upper()

if __name__ == '__main__':
 app.run(debug=True, port=5003 host='0.0.0.0')