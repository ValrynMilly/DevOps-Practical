from flask import Flask, url_for, render_template, redirect, request
from forms import titlegen

import string
import random

app = Flask(__name__)
app.config['SECRET_KEY']='Thisisanothersupersecret'

@app.route('/')
def titlegenform():
    form = titlegen(request.form)
    return render_template('titlegen.html', title='titlegen', form=form)

@app.route('/', methods=['POST'])
def titlegen_post():
    form = titlegen()
    articles = ['The', 'A']
    descriptive = ['Powerful', 'Dominant', 'Almighty', 'Omnipotent', 'Omniscient', 'Omnibenevolent', 'Ruling', 'Formidable', 'Divine' ,'Hero']
    objective = ['One', 'Demi-God', 'Giant', 'Berzerker', 'Hunter', 'Wizard', 'Born', 'God'] 
    if form.is_submitted():
        title_generated = (random.choice(articles) + " " + random.choice(descriptive) + " " + random.choice(objective)) 
        return title_generated.upper()


if __name__ == '__main__':
 app.run(debug=True, host='127.0.0.2')