from flask import Blueprint


blueprint = Blueprint("proxy", __name__)


class VoteProxy():
    def __init__(self):
        self.candidates = []

@blueprint.route('', methods=["GET"])
def index():
    return "hello"

