from application import db

class Registerfantasy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fan_name = db.Column(db.String(30), nullable=False)
    fan_title = db.Column(db.String(30), nullable=False)
    fan_story = db.Column(db.String(250), nullable=False)