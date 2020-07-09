from flask import Flask, url_for, render_template, redirect, request, Response
from application import app
import requests
import string
import random

@app.route('/', methods = ['GET', 'POST'])
def titlegen_post():
    articles = ['The', 'A']
    descriptive = ['Powerful', 'Dominant', 'Almighty', 'Omnipotent', 'Omniscient', 'Omnibenevolent', 'Ruling', 'Formidable', 'Divine' ,'Hero']
    objective = ['One', 'Demi-God', 'Giant', 'Berzerker', 'Hunter', 'Wizard', 'Born', 'God'] 
    title_generated = (random.choice(articles) + " " + random.choice(descriptive) + " " + random.choice(objective)) 
    return Response(title_generated, mimetype='type/plain')
