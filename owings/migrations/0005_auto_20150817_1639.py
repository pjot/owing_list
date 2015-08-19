# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('owings', '0004_auto_20150817_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
