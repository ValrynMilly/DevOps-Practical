#importing modules
from flask import Flask, url_for, render_template, redirect, request, Response
from application import app
import requests
import string
import random
#This route much like the others just generates a name
@app.route('/', methods = ['GET', 'POST'])
def namegenform_post():
    #There are three 3 lists, orcnames (not in use at the moment), midname and elvnames
    orcnames = ['uk', 'guk', 'keg', 'rag', 'kha', 'rok', 'zok', 'huk', 'rik']
    #orc names will be their own route soon
    midname = ['Aafke', 'Aaliyah', 'Ada', 'Adilya', 'Brynne', 'Britt', 'Cynthia', 'Halle', 'Ilana', 'Iris', 'Aaron', 'Adam', 'Alexander', 'Anton', 'Meldarion', 'Elijah', 'Eithelonnen']
    elvnames = ['iros', 'ilir', 'tris', 'aren', 'ana', 'ina', 'enys', 'ona', 'dir']
    #username value is set by randomly choosing one from each list
    username = (random.choice(elvnames) + random.choice(midname) + random.choice(elvnames))
    #then returns that value
    return Response(username, mimetype='type/plain')