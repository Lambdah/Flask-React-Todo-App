from flask_sqlalchemy import SQLAlchemy
from db import get_db

db = get_db()


class User(db):
    pass


class Task(db):
    pass


class Group(db):
    pass
