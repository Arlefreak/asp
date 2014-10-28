# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_proyect_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyect',
            name='socialText_en',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Social english', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proyect',
            name='socialText_es',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Social spanish', blank=True),
            preserve_default=True,
        ),
    ]
