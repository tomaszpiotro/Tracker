# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='title',
            field=models.CharField(max_length=128, verbose_name=b'title', blank=True),
            preserve_default=True,
        ),
    ]
