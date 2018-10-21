import flask
from flask import jsonify


class ElectionAuthority():
    def __init__(self):
        self.candidates = ["Jan Kowalski", "Janusz Nowak"]


app = flask.Flask(__name__, instance_relative_config=True)
ea_instance = ElectionAuthority()

@app.route('/')
def index():
    return "hello"


@app.route('/candidates')
def get_candidates():
    return jsonify({ "candidates" : ea_instance.candidates})


@app.route('/proxy/ballot/blind', methods=['GET', 'POST'])
def post_blinded_proxy_ballot():
    return "hello"


@app.route('/proxy/ballot/unblinded', methods=['GET', 'POST'])
def post_unblinded_proxy_ballot():
    return "hello"

@app.route('/proxy/exponents')
def get_exponents():
    return "hello"

@app.route('/proxy/tokens')
def get_tokens():
    return "hello"


def create_app():
    return app
