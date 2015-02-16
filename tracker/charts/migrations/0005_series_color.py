# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0004_auto_20150216_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='color',
            field=models.CharField(max_length=32, verbose_name=b'color', blank=True),
            preserve_default=True,
        ),
    ]
