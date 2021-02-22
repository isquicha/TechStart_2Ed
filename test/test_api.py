from flask import Flask, Response  # noqa
import json

API_URL_PREFIX = "/api/v1"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def test_get_request_on_sellers_returns_an_empty_list(client):
    res = client.get(f"{API_URL_PREFIX}/sellers/")
    assert res.status_code == 200
    assert res.json == []


def test_get_request_on_products_returns_an_empty_list(client):
    res = client.get(f"{API_URL_PREFIX}/products/")
    assert res.status_code == 200
    assert res.json == []


def test_get_request_on_categories_returns_an_empty_list(client):
    res = client.get(f"{API_URL_PREFIX}/categories/")
    assert res.status_code == 200
    assert res.json == []


def test_get_request_on_marketplaces_returns_an_empty_list(client):
    res = client.get(f"{API_URL_PREFIX}/marketplaces/")
    assert res.status_code == 200
    assert res.json == []


def test_get_request_on_sellers_returns_error_on_non_created(client):
    res: Response = client.get(f"{API_URL_PREFIX}/sellers/1")
    assert res.status_code == 400
    assert res.json == {"ERROR": "Seller does not exists"}


def test_get_request_on_products_returns_error_on_non_created(client):
    res: Response = client.get(f"{API_URL_PREFIX}/products/1")
    assert res.status_code == 400
    assert res.json == {"ERROR": "Product does not exists"}


def test_get_request_on_categories_returns_error_on_non_created(client):
    res: Response = client.get(f"{API_URL_PREFIX}/categories/1")
    assert res.status_code == 400
    assert res.json == {"ERROR": "Category does not exists"}


def test_post_request_on_category(client):
    res: Response = client.post(
        f"{API_URL_PREFIX}/categories/",
        headers=HEADERS,
        data=json.dumps({}),
    )
    assert res.status_code == 400
    assert res.json == {"ERROR": "Field 'name' must not be empty"}
