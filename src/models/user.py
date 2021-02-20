from src.extensions.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    name = db.Column(db.String(140))
    password = db.Column(db.String(512))
