# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20141015_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='order',
            field=models.PositiveSmallIntegerField(default=1, verbose_name=b'Order'),
            preserve_default=True,
        ),
    ]
