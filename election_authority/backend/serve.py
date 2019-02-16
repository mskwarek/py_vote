#!/usr/bin/env python3
from flask import Flask
from views import election_authority


def register_blueprints(app):
    app.register_blueprint(election_authority.blueprint, url_prefix="/api/ea")


def make_app(cfg_path):
    app = Flask("EA")

    register_blueprints(app)

    return app


def main():
    app = make_app("config.yml")
    app.run(host="0.0.0.0",
            port=5000,
            debug=True)



if __name__ == "__main__":
    main()


