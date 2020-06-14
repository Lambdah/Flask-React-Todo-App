import os

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db
from dotenv import load_dotenv


@pytest.fixture
def app():
    load_dotenv()
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': os.getenv("DATABASE_TEST"),
    })

    with app.app_context():
        init_db()
        get_db()   
    yield app


@pytest.fixture
def client(app):
    return app.test_client()
