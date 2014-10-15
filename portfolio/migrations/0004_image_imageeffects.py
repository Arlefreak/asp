# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20141015_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='imageEffects',
            field=models.CharField(default=b'bw', max_length=4, verbose_name=b'Effect', choices=[(b'bw', b'Black & white'), (b'one', b'Effect 1'), (b'two', b'Effect two'), (b'tre', b'Effect 3')]),
            preserve_default=True,
        ),
    ]
