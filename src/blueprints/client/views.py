from flask import render_template, url_for  # noqa


def index():
    return render_template("index.jinja2")


def sellers():
    return "sellers"


def products():
    return "products"


def categories():
    return "categories"


def marketplaces():
    return "marketplaces"
