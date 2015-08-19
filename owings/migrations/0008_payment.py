# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('owings', '0007_transaction_is_settlement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_entered', models.DateTimeField(default=datetime.datetime.now)),
                ('amount', models.FloatField()),
                ('currency', models.ForeignKey(to='owings.Currency')),
                ('from_person', models.ForeignKey(related_name='from_person', to='owings.Person')),
                ('to_person', models.ForeignKey(related_name='to_person', to='owings.Person')),
            ],
        ),
    ]
