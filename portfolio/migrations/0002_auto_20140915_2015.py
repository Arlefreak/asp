# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='imageOrientation',
            field=models.CharField(default=b'covr', max_length=4, verbose_name=b'Tipo', choices=[(b'left', b'left'), (b'rigt', b'right'), (b'cntr', b'center'), (b'covr', b'cover')]),
        ),
    ]
