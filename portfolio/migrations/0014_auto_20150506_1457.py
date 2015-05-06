# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_auto_20150427_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='imageEffect',
            field=models.CharField(default=b'no', max_length=4, verbose_name=b'Effect', choices=[(b'no', b'None'), (b'bw', b'Black & white'), (b'one', b'Effect 1'), (b'two', b'Effect 2'), (b'tre', b'Effect 3')]),
        ),
    ]
