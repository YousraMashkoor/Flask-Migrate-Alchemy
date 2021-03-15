import pytest
import os
from .app import create_app, db

os.environ['DB_USER'] = "postgres"
os.environ['DB_PASSWORD'] = "postres"
os.environ['DB_HOST'] = "localhost"
os.environ['DB_NAME'] = "testing"


@pytest.fixture
def app():
    test_app = create_app()
    yield test_app


@pytest.fixture
def client(app):
    with app.app_context():
        client = app.test_client()
        yield client

@pytest.fixture
def empty_db(app):
    with app.app_context():
        db.create_all()
        yield db

        #teardown
        db.session.remove()
        db.drop_all()

@pytest.fixture
def database(empty_db):

    yield empty_db