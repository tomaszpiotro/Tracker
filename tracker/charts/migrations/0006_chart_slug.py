# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0005_series_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='slug',
            field=models.SlugField(default='atlantiss', max_length=24, verbose_name=b'slug'),
            preserve_default=False,
        ),
    ]
