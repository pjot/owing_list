from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from owings.utils import CurrencyAPI, ExchangeRate
from owings.models import Currency

class Command(BaseCommand):
    help = 'Imports Currencies (and exchange rates against USD) from API'

    def handle(self, *args, **kwargs):
        api = CurrencyAPI(settings.CURRENCY_API_KEY)

        for rate in api.get_currencies():
            currency = self.get_currency(rate.iso_code)
            currency.iso_code = rate.iso_code
            currency.exchange_rate = rate.rate
            if currency.name == '':
                currency.name = rate.iso_code
            currency.save()

    def get_currency(self, iso_code):
        try:
            return Currency.objects.get(iso_code=iso_code)
        except Currency.DoesNotExist:
            return Currency()
