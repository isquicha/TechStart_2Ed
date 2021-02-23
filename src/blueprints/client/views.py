from flask import render_template, url_for  # noqa


def index():
    return render_template("index.jinja2")


def sellers():
    return render_template("sellers.jinja2")


def products():
    return render_template("products.jinja2")


def categories():
    return render_template("categories.jinja2")


def marketplaces():
    return render_template("marketplaces.jinja2")
