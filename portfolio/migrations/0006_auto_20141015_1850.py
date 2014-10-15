# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20141015_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='imageEffects',
        ),
        migrations.AddField(
            model_name='image',
            name='imageEffect',
            field=models.CharField(default=b'bw', max_length=4, verbose_name=b'Effect', choices=[(b'no', b'None'), (b'bw', b'Black & white'), (b'one', b'Effect 1'), (b'two', b'Effect 2'), (b'tre', b'Effect 3')]),
            preserve_default=True,
        ),
    ]
