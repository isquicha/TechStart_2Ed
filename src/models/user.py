from src.extensions.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140), unique=True, nullable=False)
    name = db.Column(db.String(140))
    password = db.Column(db.String(512), nullable=False)
