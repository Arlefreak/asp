# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20141028_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('name', models.CharField(max_length=100, verbose_name=b'Name', blank=True)),
                ('order', models.PositiveSmallIntegerField(default=1, verbose_name=b'Order')),
                ('proyect', models.ForeignKey(to='portfolio.Proyect')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
            bases=(models.Model,),
        ),
    ]
