import random
import string
import sys
import requests

from flask import Flask, url_for, render_template, redirect, request, Response

servicetwo = 'http://service-two:5001'
servicethree = 'http://service-three:5002'

app = Flask(__name__)
app.config['SECRET_KEY']='Thisisanothersuperdupersecret'

@app.route('/', methods=['GET'])
def titlegen_post():
    name = requests.get(servicetwo)
    title = requests.get(servicethree)
    where = ['In a bar','On a field', 'Through the clouds', 'Under a mountain', 'Underwater', 'In a town']
    action = ['killed', 'annihilated', 'destroyed', 'Poisoned', 'Petrified', 'Saved', 'Rescued', 'Healed', 'Silenced']
    instrument = ['a pinkie', 'a pencil', 'a hammer', 'a bow', 'lightning', 'fire', 'a hunt'] 
    shortstory = (random.choice(where) + " " + name.text + " " + title.text +" Once " + random.choice(action)+ " " + str(random.randint(1, 3000)) + " MEN WITH " + random.choice(instrument)) 
    return Response(shortstory, mimetype='text/plain')

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5003, debug=True)