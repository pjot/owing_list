from django.db import models
from datetime import datetime

class OwingList(models.Model):
    name = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=datetime.now)
    transactions = False
    payments = False

    def __unicode__(self):
        return self.name

    def get_payments(self):
        if not self.payments:
            self.payments = []
            for person in self.person_set.all():
                for payment in person.payments.all():
                    self.payments.append(payment)
        return self.payments

    def get_transactions(self):
        if not self.transactions:
            self.transactions = []
            for person in self.person_set.all():
                for transaction in person.transaction_set.all():
                    self.transactions.append(transaction)
        return self.transactions

class Person(models.Model):
    name = models.CharField(max_length=255)
    owing_list = models.ForeignKey(OwingList)

    def __unicode__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=255)
    iso_code = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    exchange_rate = models.FloatField()

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.iso_code)

    @staticmethod
    def get_active():
        return Currency.objects.filter(active=True)

class Payment(models.Model):
    date_entered = models.DateTimeField(default=datetime.now)
    from_person = models.ForeignKey(Person, related_name='payments')
    to_person = models.ForeignKey(Person)
    amount = models.FloatField()
    currency = models.ForeignKey(Currency)

    def __unicode__(self):
        values = (
            self.from_person.name,
            self.to_person.name,
            '%.2f' % self.amount,
            self.currency.iso_code,
            self.date_entered.strftime('%Y-%m-%d %H:%M')
        )
        return '%s - %s, %s %s (%s)' % values

class Transaction(models.Model):
    date_entered = models.DateTimeField(default=datetime.now)
    person = models.ForeignKey(Person)
    amount = models.FloatField()
    currency = models.ForeignKey(Currency)
    is_settlement = models.BooleanField(default=False)

    def __unicode__(self):
        values = (
            self.person.name,
            '%.2f' % self.amount,
            self.currency.iso_code,
            self.date_entered.strftime('%Y-%m-%d %H:%M')
        )
        return '%s - %s %s (%s)' % values
