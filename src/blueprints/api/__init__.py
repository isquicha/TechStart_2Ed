from flask import Blueprint

from .routes import user

bp = Blueprint("api", __name__, url_prefix="/api/v1")

user.init_app(bp)


def init_app(app):
    app.register_blueprint(bp)
