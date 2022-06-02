from bitcoin_price import BitcoinPrice
import pytest, requests, re

def test_init():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    assert requests.get(url)

def test_req_data():
    dict = BitcoinPrice._req_data(url, url)
    assert "USD" in dict

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
print(BitcoinPrice._req_data(url, url))