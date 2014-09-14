# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import portfolio.models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('idImage', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nombre', blank=True)),
                ('image', models.ImageField(upload_to=portfolio.models.upload_image_to, null=True, verbose_name=b'Imagen', blank=True)),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imagenes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('mainImage', models.ImageField(upload_to=portfolio.models.upload_image_to, verbose_name=b'Imagen principal')),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Elemento de prensa',
                'verbose_name_plural': 'Elementos de prensa',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proyect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name=b'Name')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name=b'Updated')),
                ('mainImage', models.ImageField(upload_to=portfolio.models.upload_image_to, verbose_name=b'Main Image')),
                ('decondImage', models.ImageField(upload_to=portfolio.models.upload_image_to, verbose_name=b'Second Image', blank=True)),
                ('published', models.BooleanField(default=False, verbose_name=b'Published')),
                ('slug', models.SlugField(max_length=100, verbose_name=b'Slug Name')),
            ],
            options={
                'verbose_name': 'Proyect',
                'verbose_name_plural': 'Proyects',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='singleInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aboutImage', models.ImageField(upload_to=portfolio.models.upload_image_to, verbose_name=b'Imagen about')),
                ('aboutText', ckeditor.fields.RichTextField()),
                ('line1', models.CharField(max_length=140, null=True, verbose_name=b'linea 1', blank=True)),
                ('line2', models.CharField(max_length=140, null=True, verbose_name=b'linea 2', blank=True)),
                ('line3', models.CharField(max_length=140, null=True, verbose_name=b'linea 3', blank=True)),
                ('line4', models.CharField(max_length=140, null=True, verbose_name=b'linea 4', blank=True)),
                ('published', models.BooleanField(default=False, verbose_name=b'Publicado')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='proyect',
            field=models.ForeignKey(to='portfolio.Proyect'),
            preserve_default=True,
        ),
    ]
