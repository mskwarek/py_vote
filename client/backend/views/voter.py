from flask import (jsonify, Blueprint)


blueprint = Blueprint("/voter", __name__)


@blueprint.route("", methods=["GET"])
def index():
    return jsonify({})
