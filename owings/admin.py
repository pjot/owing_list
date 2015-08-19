from django.contrib import admin
from .models import Person, OwingList, Currency, Transaction, Payment

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso_code', 'exchange_rate')

admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Person)
admin.site.register(OwingList)
admin.site.register(Transaction)
admin.site.register(Payment)
