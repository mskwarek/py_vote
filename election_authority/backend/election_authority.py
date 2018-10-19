import flask
from flask import jsonify

app = flask.Flask(__name__, instance_relative_config=True)
class ElectionAuthority():
    def __init__(self):
        self.candidates = []

@app.route('/')
def index():
    return "hello"


@app.route('/candidates')
def get_candidates():
    return jsonify({ "candidates" : [""]})


@app.route('/proxy/ballot/blind', methods=['GET', 'POST'])
def post_blinded_proxy_ballot():
    return "hello"


@app.route('/proxy/ballot/unblinded', methods=['GET', 'POST'])
def post_unblinded_proxy_ballot():
    return "hello"


def create_app():
    return app