import json

from . import API_URL_PREFIX, HEADERS

URL = API_URL_PREFIX + "/categories"


def test_get_request_returns_an_empty_list(client):
    res = client.get(f"{URL}/")
    assert res.status_code == 200
    assert res.json == []


def test_get_request_returns_error_on_non_created(client):
    res = client.get(f"{URL}/1")
    assert res.status_code == 400
    assert res.json == {"ERROR": "Category does not exists"}


def test_post_request_fail_when_parameters_are_not_provided(client):
    res = client.post(
        f"{URL}/",
        headers=HEADERS,
        data=json.dumps({}),
    )
    assert res.status_code == 400
    assert res.json == {"ERROR": "Field 'name' must not be empty"}
