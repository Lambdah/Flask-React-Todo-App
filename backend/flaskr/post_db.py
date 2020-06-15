from flask import current_app
from flask import g
from flaskr import db
from flask.cli import with_appcontext
import click


def get_db():
    """
    Connects to the database. Each connection is unique
    """
    if "db" not in g:
        g.db = db
    return g.db


def close_db(e=None):
    """
    Closes the connection to the database
    """
    db = g.pop('db', None)

    if db is not None:
        db.session.close()


def init_db():
    """
    Clears the existing tables and creates new tables
    """
    db = get_db()
    db.create_all()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """
    Wipes the database and start anew
    """
    init_db()
    click.echo("Initializing a new database")


def init_db_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
