# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='press',
            name='url',
            field=models.URLField(default=datetime.date(2015, 2, 7), verbose_name=b'URL'),
            preserve_default=False,
        ),
    ]
