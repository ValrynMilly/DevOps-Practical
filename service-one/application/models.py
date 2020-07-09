from application import db

class Registerfantasy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fan_name = db.Column(db.String(5), nullable=False)
    fan_title = db.Column(db.String(5), nullable=False)
    fan_story = db.Column(db.String(500), nullable=False)