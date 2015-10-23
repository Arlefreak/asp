# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_sociallinks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(verbose_name='Image', upload_to=portfolio.models.upload_image_to),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageEffect',
            field=models.CharField(choices=[('no', 'None'), ('bw', 'Black & white'), ('one', 'Effect 1'), ('two', 'Effect 2'), ('tre', 'Effect 3')], default='no', max_length=4, verbose_name='Effect'),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageOrientation',
            field=models.CharField(choices=[('left', 'left'), ('rigt', 'right'), ('cntr', 'center'), ('covr', 'cover')], default='covr', max_length=4, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='press',
            name='mainImage',
            field=models.ImageField(verbose_name='Main image', upload_to=portfolio.models.upload_image_to),
        ),
        migrations.AlterField(
            model_name='press',
            name='name_en',
            field=models.CharField(max_length=140, verbose_name='Name english'),
        ),
        migrations.AlterField(
            model_name='press',
            name='name_es',
            field=models.CharField(max_length=140, verbose_name='Name spanish'),
        ),
        migrations.AlterField(
            model_name='press',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Created', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='press',
            name='url',
            field=models.URLField(verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='date',
            field=models.CharField(max_length=140, verbose_name='Fechas', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='home',
            field=models.BooleanField(default=False, verbose_name='Home'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='imageOrientation',
            field=models.CharField(choices=[('left', 'left'), ('rigt', 'right'), ('up', 'up'), ('down', 'down'), ('cntr', 'center')], default='cntr', max_length=4, verbose_name='Alignment'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='location',
            field=models.CharField(max_length=140, verbose_name='Location', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='mainImage',
            field=models.ImageField(verbose_name='Main Image', upload_to=portfolio.models.upload_image_to),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='name_en',
            field=models.CharField(max_length=140, verbose_name='Name english', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='name_es',
            field=models.CharField(max_length=140, verbose_name='Name spanish'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='order',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='proyects',
            field=models.BooleanField(default=False, verbose_name='Proyects'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Created', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='secondImage',
            field=models.ImageField(verbose_name='Second Image', upload_to=portfolio.models.upload_image_to, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Slug Name'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='socialText_en',
            field=models.CharField(max_length=100, verbose_name='Social english', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='socialText_es',
            field=models.CharField(max_length=100, verbose_name='Social spanish', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='singleinformation',
            name='aboutImage',
            field=models.ImageField(verbose_name='Imagen about', upload_to=portfolio.models.upload_image_to),
        ),
        migrations.AlterField(
            model_name='singleinformation',
            name='line1',
            field=models.CharField(max_length=140, verbose_name='linea 1', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='singleinformation',
            name='line2',
            field=models.CharField(max_length=140, verbose_name='linea 2', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='singleinformation',
            name='line3',
            field=models.CharField(max_length=140, verbose_name='linea 3', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='singleinformation',
            name='line4',
            field=models.CharField(max_length=140, verbose_name='linea 4', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='singleinformation',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='sociallinks',
            name='fb',
            field=models.URLField(verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='sociallinks',
            name='it',
            field=models.URLField(verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='sociallinks',
            name='tw',
            field=models.URLField(verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name', blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='order',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Order'),
        ),
    ]
