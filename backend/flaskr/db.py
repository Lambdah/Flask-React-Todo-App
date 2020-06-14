from flask import current_app
from flask import g
from flask_sqlalchemy import SQLAlchemy


def get_db():
    """
    Connects to the database. Each connection is unique
    """
    if "db" not in g:
        g.db = SQLAlchemy(current_app)
    return g.db


def close_db(e=None):
    """
    Closes the connection to the database
    """
    pass


def init_db():
    """
    Clears the existing tables and creates new tables
    """
    db = get_db()
    db.create_all()
