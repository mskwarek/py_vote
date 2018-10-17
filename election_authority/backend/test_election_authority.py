import pytest
import flask
import election_authority


@pytest.fixture
def client():
    flask_app = election_authority.create_app()
    client = flask_app.test_client()
    yield client

def test_empty_db(client):
    rv = client.get('/')
    assert 200 == rv.status_code

def test_get_candidate_list_endpoint(client):
    rv = client.get('/candidates')
    assert 200 == rv.status_code

def test_blind_proxy_ballot_endpoint(client):
    rv = client.get('/proxy/ballot/blind')
    assert 200 == rv.status_code

