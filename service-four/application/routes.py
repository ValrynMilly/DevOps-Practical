#Importing modules
from flask import Flask, url_for, render_template, redirect, request, Response
from application import app
import requests
import string
import random
#predefining where services
servicetwo = 'http://service-two:5001'
servicethree = 'http://service-three:5002'

@app.route('/', methods = ['GET', 'POST'])
def titlegen_post():
    #Name is defined then makes a request to service two to give it a value
    name = requests.get(servicetwo)
    #title is defined then makes a request to service thee to give it a value
    title = requests.get(servicethree)
    intro = "Once upon a time"
    where = ['In a bar','On a field', 'Through the clouds', 'Under a mountain', 'Underwater', 'In a town']
    action = ['killed', 'annihilated', 'destroyed', 'Poisoned', 'Petrified', 'Saved', 'Rescued', 'Healed', 'Silenced']
    instrument = ['a pinkie', 'a pencil', 'a hammer', 'a bow', 'lightning', 'fire', 'a hunt'] 
    #short story is a combination of lists randomly picked but within the story name and title are reference so the result makes sense
    shortstory = (intro + random.choice(where) + " " + name.text + " " + title.text +" Once " + random.choice(action)+ " " + str(random.randint(1, 3000)) + " MEN WITH " + random.choice(instrument)) 
    #then returns a response with the short story
    return Response(shortstory.upper(), mimetype='text/plain')