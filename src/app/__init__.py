from flask import Flask

from src.extensions.configuration import configure


def create_app():
    app = Flask(__name__)
    configure(app)
    return app
