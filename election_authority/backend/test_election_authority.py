import pytest
import flask
import election_authority
import json


@pytest.fixture
def client():
    flask_app = election_authority.create_app()
    client = flask_app.test_client()
    yield client

def test_default_get(client):
    rv = client.get('/')
    assert 200 == rv.status_code

def test_rc_get_candidate_list_endpoint(client):
    rv = client.get('/candidates')
    assert 200 == rv.status_code


def test_get_non_empty_candidate_list_endpoint(client):
    rv = client.get('/candidates')
    data = json.loads(rv.get_data(as_text=True))
    assert 200 == rv.status_code
    assert data != None


def test_blind_proxy_ballot_endpoint(client):
    rv = client.post('/proxy/ballot/blind')
    assert 200 == rv.status_code

def test_post_unblinded_proxy_ballot_endpoint(client):
    rv = client.post('/proxy/ballot/unblinded')
    assert 200 == rv.status_code

