# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('charts', '0002_series_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='httpseries',
            name='series_ptr',
        ),
        migrations.AddField(
            model_name='series',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_charts.series_set', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
    ]
