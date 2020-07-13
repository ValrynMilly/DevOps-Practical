#importing modules
from flask import Flask, url_for, render_template, redirect, request, Response
from application import app
import requests
import string
import random

#First route creates a title much like name and story is done
@app.route('/', methods = ['GET', 'POST'])
def titlegen_post():
    #Here we see three lists articles, descriptive & adjectives. Full of a variety of relevant values 
    articles = ['The', 'A']
    descriptive = ['Powerful', 'Dominant', 'Almighty', 'Omnipotent', 'Omniscient', 'Omnibenevolent', 'Ruling', 'Formidable', 'Divine' ,'Hero']
    objective = ['One', 'Demi-God', 'Giant', 'Berzerker', 'Hunter', 'Wizard', 'Born', 'God']
    #Title generated randomly chooses one from all three and combines them to make a title. 
    title_generated = (random.choice(articles) + " " + random.choice(descriptive) + " " + random.choice(objective)) 
    #Then returns that title
    return Response(title_generated, mimetype='type/plain')
