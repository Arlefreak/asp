# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_press_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='press',
            options={'verbose_name': 'Noticia', 'verbose_name_plural': 'Noticias'},
        ),
        migrations.AlterField(
            model_name='proyect',
            name='secondImage',
            field=models.ImageField(upload_to=portfolio.models.upload_image_to, null=True, verbose_name=b'Second Image', blank=True),
        ),
    ]
