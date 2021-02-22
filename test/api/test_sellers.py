import json

from . import API_URL_PREFIX, HEADERS

URL = API_URL_PREFIX + "/sellers"
seller_1 = {
    "id": 1,
    "fantasy_name": "Fantasy Name",
    "company_name": "Company Name",
    "tax_code": "123456789",
    "email": "mail@example.com",
    "phone": "123456789",
    "address": "Example St. N 773",
}


def test_get_request_returns_an_empty_list(client):
    res = client.get(f"{URL}/")
    assert res.status_code == 200
    assert res.json == []


def test_get_request_returns_error_on_non_created(client):
    res = client.get(f"{URL}/1")
    assert res.status_code == 400
    assert res.json == {"ERROR": "Seller does not exists"}


def test_post_request_fail_when_parameters_are_not_provided_1(client):
    res = client.post(
        f"{URL}/",
        headers=HEADERS,
        data=json.dumps({}),
    )
    assert res.status_code == 400
    assert res.json == {"ERROR": "Field 'fantasy_name' must not be empty"}


def test_post_request_fail_when_parameters_are_not_provided_2(client):
    res = client.post(
        f"{URL}/",
        headers=HEADERS,
        data=json.dumps({"fantasy_name": "Fantasy Name"}),
    )
    assert res.status_code == 400
    assert res.json == {"ERROR": "Field 'company_name' must not be empty"}


def test_post_request_fail_when_parameters_are_not_provided_3(client):
    res = client.post(
        f"{URL}/",
        headers=HEADERS,
        data=json.dumps(
            {"fantasy_name": "Fantasy Name", "company_name": "Company Name"}
        ),
    )
    assert res.status_code == 400
    assert res.json == {"ERROR": "Field 'tax_code' must not be empty"}


def test_post_request_fail_when_parameters_are_not_provided_4(client):
    res = client.post(
        f"{URL}/",
        headers=HEADERS,
        data=json.dumps(
            {
                "fantasy_name": "Fantasy Name",
                "company_name": "Company Name",
                "tax_code": "123456789",
            }
        ),
    )
    assert res.status_code == 400
    assert res.json == {"ERROR": "Field 'email' must not be empty"}


def test_post_request_fail_when_parameters_are_not_provided_5(client):
    res = client.post(
        f"{URL}/",
        headers=HEADERS,
        data=json.dumps(
            {
                "fantasy_name": "Fantasy Name",
                "company_name": "Company Name",
                "tax_code": "123456789",
                "email": "mail@example.com",
            }
        ),
    )
    assert res.status_code == 400
    assert res.json == {"ERROR": "Field 'phone' must not be empty"}


def test_post_request_fail_when_parameters_are_not_provided_6(client):
    res = client.post(
        f"{URL}/",
        headers=HEADERS,
        data=json.dumps(
            {
                "fantasy_name": "Fantasy Name",
                "company_name": "Company Name",
                "tax_code": "123456789",
                "email": "mail@example.com",
                "phone": "123456789",
            }
        ),
    )
    assert res.status_code == 400
    assert res.json == {"ERROR": "Field 'address' must not be empty"}


def test_post_request_returns_ok(client):
    res = client.post(
        f"{URL}/",
        headers=HEADERS,
        data=json.dumps(
            {
                "fantasy_name": "Fantasy Name",
                "company_name": "Company Name",
                "tax_code": "123456789",
                "email": "mail@example.com",
                "phone": "123456789",
                "address": "Example St. N 773",
            }
        ),
    )
    assert res.status_code == 200
    assert res.json == {"id": 1, "fantasy_name": "Fantasy Name"}


def test_get_request_returns_ok(client):
    res = client.get(f"{URL}/1")
    assert res.status_code == 200
    assert res.json == seller_1


def test_patch_request_returns_same_on_blank_body(client):
    res = client.patch(
        f"{URL}/1",
        headers=HEADERS,
        data=json.dumps({}),
    )
    assert res.status_code == 200
    assert res.json == seller_1


def test_patch_request_returns_ok_on_fantasy_name_update(client):
    res = client.patch(
        f"{URL}/1",
        headers=HEADERS,
        data=json.dumps({"fantasy_name": "Fantasy Name 2"}),
    )
    seller_1["fantasy_name"] = "Fantasy Name 2"
    assert res.status_code == 200
    assert res.json == seller_1


def test_patch_request_returns_ok_on_company_name_update(client):
    res = client.patch(
        f"{URL}/1",
        headers=HEADERS,
        data=json.dumps({"company_name": "Company Name 2"}),
    )
    seller_1["company_name"] = "Company Name 2"
    assert res.status_code == 200
    assert res.json == seller_1
