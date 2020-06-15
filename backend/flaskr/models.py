from flask_sqlalchemy import SQLAlchemy
from flaskr import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    alias = db.Column(db.String(80), nullable=True)


# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)


# class Group(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
