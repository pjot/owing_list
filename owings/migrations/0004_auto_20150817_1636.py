# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owings', '0003_currency_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_entered',
            field=models.DateTimeField(),
        ),
    ]
