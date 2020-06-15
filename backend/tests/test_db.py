import pytest
from flaskr.db import get_db
from flask_sqlalchemy import SQLAlchemy


def test_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()
    with pytest.raises(SQLAlchemy.ProgrammingError) as e:
        db.session.execute('SELECT 1')

    assert 'closed' in str(e.value)
