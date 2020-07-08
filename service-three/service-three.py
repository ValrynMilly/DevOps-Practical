from flask import Flask, url_for, render_template, redirect, request
import requests
import string
import random

app = Flask(__name__)
app.config['SECRET_KEY']='Thisisanothersupersecret'

@app.route('/', methods=['GET'])
def titlegen_post():
    articles = ['The', 'A']
    descriptive = ['Powerful', 'Dominant', 'Almighty', 'Omnipotent', 'Omniscient', 'Omnibenevolent', 'Ruling', 'Formidable', 'Divine' ,'Hero']
    objective = ['One', 'Demi-God', 'Giant', 'Berzerker', 'Hunter', 'Wizard', 'Born', 'God'] 
    title_generated = (random.choice(articles) + " " + random.choice(descriptive) + " " + random.choice(objective)) 
    return title_generated.upper()

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5002, debug=True)