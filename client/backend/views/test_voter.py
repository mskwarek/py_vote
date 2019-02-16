import pytest
import flask
import voter


@pytest.fixture
def client():
    flask_app = voter.create_app()
    client = flask_app.test_client()

    yield client

def test_empty_db(client):
    rv = client.get('/')
    assert 200 == rv.status_code
