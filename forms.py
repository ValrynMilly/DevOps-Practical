from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired

class titlegen(FlaskForm):
    #Title generation
    submit = SubmitField('Generate')