import flask 


app = flask.Flask(__name__, instance_relative_config=True)
class Voter():
    def __init__(self):
        self.candidates = []

@app.route('/')
def index():
    return "Hello"

def create_app():
    return app