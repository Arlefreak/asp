# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20141028_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=portfolio.models.upload_image_to, verbose_name=b'Image'),
        ),
    ]
