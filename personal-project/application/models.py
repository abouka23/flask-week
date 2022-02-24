from sqlalchemy import ForeignKey
from application import db


class Characters(db.Model):
    character_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    date= db.Column(db.Date, nullable=False)
    description = db.Column(db.String(30),nullable=False)
    completed = db.Column(db.Boolean , default=False)
    #class_id = db.Column(db.Integer, db.ForeignKey('Classes.id'), nullable = False)
