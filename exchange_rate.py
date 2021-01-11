import urllib.request as req
from json import loads


class Currency:
    base_url: str = "https://api.exchangeratesapi.io"
    timeout: int = 10
    codes = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS',
             'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB',
             'TRY', 'USD', 'ZAR']

    def __init__(self, my_dict: dict):
        self.base_currency = my_dict['base']
        self.date = my_dict['date']
        self.rates = my_dict['rates']

    def convert_amount_to(self, amount, to: str):
        return amount * self.rates.get(to)


def get_all_for_base(a: str) -> dict:
    local_url = Currency.base_url + '/latest?base=' + a
    try:
        with req.urlopen(local_url, timeout=10) as f:
            json_data: dict = loads(f.read())
    except Exception as e:
        print(e, local_url)
    return json_data
