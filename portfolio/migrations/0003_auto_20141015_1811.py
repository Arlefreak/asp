# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20140915_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyect',
            name='published',
        ),
        migrations.AddField(
            model_name='proyect',
            name='home',
            field=models.BooleanField(default=False, verbose_name=b'Home'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proyect',
            name='proyects',
            field=models.BooleanField(default=False, verbose_name=b'Proyects'),
            preserve_default=True,
        ),
    ]
