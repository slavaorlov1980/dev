from bitcoin_price import BitcoinPrice
import pytest, requests


def test_url():                        # тест ответа от сервера
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    assert requests.get(url).status_code == 200


@pytest.mark.parametrize("currency", ("USD", "EUR", "GBP"))
def test__req_data(currency):            # тест на содержание в json ключей валют
    dict = BitcoinPrice._req_data(req, url)
    assert currency in dict


# def test_raw_data():
#     pass


# def test_btc_calculate():
#     pass


# def test__bit_convert():
#     pass


# def test__get_rate():
#     pass


# def test_get_rate():
#     pass


# def test__btc_calculate():
#     pass


# def test__result():
#     pass


# def test_print_to_console():
#     pass


# def test_add_to_log():
#     pass


url = "https://api.coindesk.com/v1/bpi/currentprice.json"
req = BitcoinPrice(url)
print(BitcoinPrice._req_data(req, url))