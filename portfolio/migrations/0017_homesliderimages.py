# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_auto_20151023_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSliderImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL')),
                ('image', models.ImageField(upload_to=portfolio.models.upload_image_to, verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
