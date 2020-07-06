from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired

class storygen(FlaskForm):
    #Story generation
    submit = SubmitField('Generate')