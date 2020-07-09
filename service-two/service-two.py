from flask import Flask, url_for, render_template, redirect, request, Response
import string
import random
import requests

app = Flask(__name__)
app.config['SECRET_KEY']='Thisissecret'

@app.route('/', methods = ['GET', 'POST'])
def namegenform_post():
    orcnames = ['uk', 'guk', 'keg', 'rag', 'kha', 'rok', 'zok', 'huk', 'rik']
    #orc names will be their own route soon
    midname = ['Aafke', 'Aaliyah', 'Ada', 'Adilya', 'Brynne', 'Britt', 'Cynthia', 'Halle', 'Ilana', 'Iris', 'Aaron', 'Adam', 'Alexander', 'Anton', 'Meldarion', 'Elijah', 'Eithelonnen']
    elvnames = ['iros', 'ilir', 'tris', 'aren', 'ana', 'ina', 'enys', 'ona', 'dir']
    username = (random.choice(elvnames) + random.choice(midname) + random.choice(elvnames))
    return Response(username, mimetype='type/plain')


if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5001, debug=True)
