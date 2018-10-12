import flask


app = flask.Flask(__name__, instance_relative_config=True)
class ElectionAuthority():
    def __init__(self):
        self.candidates = []

@app.route('/')
def index():
    return "hello"


def create_app():
    return app