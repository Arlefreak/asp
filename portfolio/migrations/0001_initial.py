# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models

import portfolio.models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('idImage', models.AutoField(
                    serialize=False, primary_key=True)),
                ('name',
                 models.CharField(
                     max_length=100, verbose_name=b'Name', blank=True)),
                ('image',
                 models.ImageField(
                     upload_to=portfolio.models.upload_image_to,
                     null=True,
                     verbose_name=b'Image',
                     blank=True)),
                ('imageOrientation',
                 models.CharField(
                     default=b'covr',
                     max_length=4,
                     verbose_name=b'Tipo',
                     choices=[(b'left', b'left'), (b'rigt', b'right'),
                              (b'up', b'up'), (b'down', b'down'),
                              (b'cntr', b'center'), (b'covr', b'cover')])),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imagenes',
            },
            bases=(models.Model, ),
        ),
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id',
                 models.AutoField(
                     verbose_name='ID',
                     serialize=False,
                     auto_created=True,
                     primary_key=True)),
                ('name_es',
                 models.CharField(
                     max_length=140, verbose_name=b'Name spanish')),
                ('name_en',
                 models.CharField(
                     max_length=140, verbose_name=b'Name english')),
                ('mainImage',
                 models.ImageField(
                     upload_to=portfolio.models.upload_image_to,
                     verbose_name=b'Main image')),
                ('description_es', ckeditor.fields.RichTextField()),
                ('description_en', ckeditor.fields.RichTextField()),
                ('pub_date',
                 models.DateTimeField(
                     auto_now_add=True, verbose_name=b'Created')),
            ],
            options={
                'verbose_name': 'Elemento de prensa',
                'verbose_name_plural': 'Elementos de prensa',
            },
            bases=(models.Model, ),
        ),
        migrations.CreateModel(
            name='Proyect',
            fields=[
                ('id',
                 models.AutoField(
                     verbose_name='ID',
                     serialize=False,
                     auto_created=True,
                     primary_key=True)),
                ('name_es',
                 models.CharField(
                     max_length=140, verbose_name=b'Name spanish')),
                ('name_en',
                 models.CharField(
                     max_length=140,
                     null=True,
                     verbose_name=b'Name english',
                     blank=True)),
                ('location',
                 models.CharField(
                     max_length=140,
                     null=True,
                     verbose_name=b'Location',
                     blank=True)),
                ('date',
                 models.CharField(
                     max_length=140,
                     null=True,
                     verbose_name=b'Fechas',
                     blank=True)),
                ('description_es', ckeditor.fields.RichTextField()),
                ('description_en', ckeditor.fields.RichTextField()),
                ('pub_date',
                 models.DateTimeField(
                     auto_now_add=True, verbose_name=b'Created')),
                ('mainImage',
                 models.ImageField(
                     upload_to=portfolio.models.upload_image_to,
                     verbose_name=b'Main Image')),
                ('secondImage',
                 models.ImageField(
                     upload_to=portfolio.models.upload_image_to,
                     verbose_name=b'Second Image',
                     blank=True)),
                ('imageOrientation',
                 models.CharField(
                     default=b'cntr',
                     max_length=4,
                     verbose_name=b'Alignment',
                     choices=[(b'left', b'left'), (b'rigt', b'right'), (b'up',
                                                                        b'up'),
                              (b'down', b'down'), (b'cntr', b'center')])),
                ('published',
                 models.BooleanField(default=False,
                                     verbose_name=b'Published')),
                ('slug',
                 models.SlugField(max_length=100, verbose_name=b'Slug Name')),
            ],
            options={
                'verbose_name': 'Proyect',
                'verbose_name_plural': 'Proyects',
            },
            bases=(models.Model, ),
        ),
        migrations.CreateModel(
            name='singleInformation',
            fields=[
                ('id',
                 models.AutoField(
                     verbose_name='ID',
                     serialize=False,
                     auto_created=True,
                     primary_key=True)),
                ('aboutImage',
                 models.ImageField(
                     upload_to=portfolio.models.upload_image_to,
                     verbose_name=b'Imagen about')),
                ('aboutText_es', ckeditor.fields.RichTextField()),
                ('aboutText_en', ckeditor.fields.RichTextField()),
                ('line1',
                 models.CharField(
                     max_length=140,
                     null=True,
                     verbose_name=b'linea 1',
                     blank=True)),
                ('line2',
                 models.CharField(
                     max_length=140,
                     null=True,
                     verbose_name=b'linea 2',
                     blank=True)),
                ('line3',
                 models.CharField(
                     max_length=140,
                     null=True,
                     verbose_name=b'linea 3',
                     blank=True)),
                ('line4',
                 models.CharField(
                     max_length=140,
                     null=True,
                     verbose_name=b'linea 4',
                     blank=True)),
                ('published',
                 models.BooleanField(default=False,
                                     verbose_name=b'Published')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
            bases=(models.Model, ),
        ),
        migrations.AddField(
            model_name='image',
            name='proyect',
            field=models.ForeignKey(
                to='portfolio.Proyect', on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
