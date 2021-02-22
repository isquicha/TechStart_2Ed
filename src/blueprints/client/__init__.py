from flask import Blueprint
from .views import index, sellers, products, categories, marketplaces

bp = Blueprint("client", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/sellers", view_func=sellers)
bp.add_url_rule("/products", view_func=products)
bp.add_url_rule("/categories", view_func=categories)
bp.add_url_rule("/marketplaces", view_func=marketplaces)


def init_app(app):
    app.register_blueprint(bp)
