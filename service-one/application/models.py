#importing database that was declared
from application import db
#Below is the database variables, simple 4 colums
class Registerfantasy(db.Model):
    #ID column for identification of each commit
    id = db.Column(db.Integer, primary_key=True)
    #Name column from generated content
    fan_name = db.Column(db.String(30), nullable=False)
    #title column from generated content
    fan_title = db.Column(db.String(30), nullable=False)
    #story column from generated content
    fan_story = db.Column(db.String(250), nullable=False)