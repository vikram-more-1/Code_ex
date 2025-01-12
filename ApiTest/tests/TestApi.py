import requests
import pytest


@pytest.fixture
def coindesk_setup():
    return requests.get(url="https://api.coindesk.com/v1/bpi/currentprice.json")


def test_R001(coindesk_setup):
    resp = coindesk_setup.json()["bpi"]
    assert "USD" in resp
    assert "GBP" in resp
    assert "EUR" in resp


def test_R002(coindesk_setup):
    gbp_desc = coindesk_setup.json()["bpi"]["GBP"]["description"]
    assert gbp_desc == "British Pound Sterling"
