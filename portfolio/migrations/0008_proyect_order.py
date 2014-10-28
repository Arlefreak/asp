# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_image_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyect',
            name='order',
            field=models.PositiveSmallIntegerField(default=1, verbose_name=b'Order'),
            preserve_default=True,
        ),
    ]
