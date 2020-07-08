from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired

class namegen(FlaskForm):
    # Name generation form
    first_name = StringField('First Name', [
        DataRequired()])
    last_name = StringField('Last_name', [
        DataRequired()])
    submit = SubmitField('Submit')