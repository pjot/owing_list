# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owings', '0006_auto_20150818_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_settlement',
            field=models.BooleanField(default=False),
        ),
    ]
