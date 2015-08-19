# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owings', '0008_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currency',
            name='exchange_rate',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='from_person',
            field=models.ForeignKey(related_name='payments', to='owings.Person'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='to_person',
            field=models.ForeignKey(to='owings.Person'),
        ),
    ]
