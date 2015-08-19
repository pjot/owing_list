import requests
import json

class ExchangeRate(object):
    iso_code = ''
    rate = 0.0

    def __init__(self, iso_code, rate):
        self.iso_code = iso_code
        self.rate = float(rate)

class CurrencyAPI(object):
    api_key = ''
    url = 'https://openexchangerates.org/api/latest.json?app_id=%s'

    def __init__(self, api_key):
        self.api_key = api_key

    def get_currencies(self):
        url = self.url % self.api_key

        response = json.loads(requests.get(url).text)
        for iso_code, rate in response['rates'].iteritems():
           yield ExchangeRate(iso_code, rate)
