from flask import (Blueprint, jsonify)
from authority import serial_numbers_generator

blueprint = Blueprint("ea", __name__)


class ElectionAuthority():
    def __init__(self):
        self.candidates = ["Jan Kowalski", "Janusz Nowak", "Candidate First", "Candidate Second",
            "Candidate Third"]

ea_instance = ElectionAuthority()


@blueprint.route('/')
def index():
    return "hello"


@blueprint.route('/candidates')
def get_candidates():
    return jsonify({ "candidates" : ea_instance.candidates})


@blueprint.route('/ballot/blind', methods=['GET', 'POST'])
def post_blinded_proxy_ballot():
    return "hello"


@blueprint.route('/ballot/unblinded', methods=['GET', 'POST'])
def post_unblinded_proxy_ballot():
    return "hello"


@blueprint.route('/exponents')
def get_exponents():
    return "hello"


@blueprint.route('/tokens')
def get_tokens():
    return "hello"
