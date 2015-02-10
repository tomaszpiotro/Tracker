# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='httpseries',
            name='html_class',
            field=models.CharField(max_length=64, null=True, verbose_name=b'class', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='httpseries',
            name='html_id',
            field=models.CharField(max_length=64, null=True, verbose_name=b'id', blank=True),
            preserve_default=True,
        ),
    ]
