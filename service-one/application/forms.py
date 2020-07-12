#import modules
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired

class namegen(FlaskForm):
    # Name generation form
    submit = SubmitField('Submit')