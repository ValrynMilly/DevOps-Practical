from application import db
from application.models import Registerfantasy


db.drop_all()
db.create_all()