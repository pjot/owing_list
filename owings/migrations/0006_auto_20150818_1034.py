# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('owings', '0005_auto_20150817_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owinglist',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
