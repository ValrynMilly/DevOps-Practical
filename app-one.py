from flask import Flask, url_for, render_template, redirect, request

from forms import namegen
import string
import random

app = Flask(__name__)
app.config['SECRET_KEY']='Thisissecret'

@app.route('/')
def namegenform():
    form = namegen(request.form)
    return render_template('namegen.html', title='namegen', form=form)

@app.route('/', methods=['POST'])
def namegenform_post():
    form = namegen()
    orcnames = ['uk', 'guk', 'keg', 'rag', 'kha', 'rok', 'zok', 'huk', 'rik']
    #orc names will be their own route soon
    elvnames = ['iros', 'ilir', 'tris', 'aren', 'ana', 'ina', 'enys', 'ona', 'dir']
    if form.is_submitted():
        firstname = request.form.get('first_name')
        lastname = request.form.get('last_name')
        genfirst = firstname[:2]
        gensecond = lastname[:3]
        username = (random.choice(elvnames) + genfirst + gensecond + random.choice(elvnames)) 
        return username.upper()


if __name__ == '__main__':
 app.run(debug=True, host='127.0.0.1')