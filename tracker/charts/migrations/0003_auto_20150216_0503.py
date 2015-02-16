# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0002_auto_20150212_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='type',
            field=models.CharField(default='line', max_length=128, verbose_name=b'type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='x_axis_name',
            field=models.CharField(default='date', max_length=32, verbose_name=b'x axis name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='y_axis_name',
            field=models.CharField(default='Online', max_length=32, verbose_name=b'y axis name'),
            preserve_default=False,
        ),
    ]
