# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='owing_list',
            field=models.ForeignKey(default='', to='owings.OwingList'),
            preserve_default=False,
        ),
    ]
