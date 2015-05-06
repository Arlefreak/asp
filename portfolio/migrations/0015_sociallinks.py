# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20150506_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fb', models.URLField(verbose_name=b'Facebook')),
                ('tw', models.URLField(verbose_name=b'Twitter')),
                ('it', models.URLField(verbose_name=b'Instagram')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
