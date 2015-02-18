# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name=b'title')),
                ('type', models.CharField(max_length=128, verbose_name=b'type')),
                ('x_axis_name', models.CharField(max_length=32, verbose_name=b'x axis name')),
                ('y_axis_name', models.CharField(max_length=32, verbose_name=b'y axis name')),
                ('slug', models.SlugField(default=b'', max_length=24, verbose_name=b'slug')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Probe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'datetime')),
                ('value', models.IntegerField(verbose_name=b'value')),
            ],
            options={
                'ordering': ['date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name=b'name')),
                ('color', models.CharField(max_length=32, verbose_name=b'color', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HttpSeries',
            fields=[
                ('series_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='charts.Series')),
                ('url', models.URLField(verbose_name=b'url')),
                ('tag', models.CharField(max_length=32, null=True, verbose_name=b'tag')),
                ('html_id', models.CharField(max_length=64, null=True, verbose_name=b'id', blank=True)),
                ('html_class', models.CharField(max_length=64, null=True, verbose_name=b'class', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('charts.series', models.Model),
        ),
        migrations.CreateModel(
            name='NestedSeries',
            fields=[
                ('httpseries_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='charts.HttpSeries')),
            ],
            options={
                'abstract': False,
            },
            bases=('charts.httpseries',),
        ),
        migrations.CreateModel(
            name='ThirdNextSibling',
            fields=[
                ('nestedseries_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='charts.NestedSeries')),
            ],
            options={
                'abstract': False,
            },
            bases=('charts.nestedseries',),
        ),
        migrations.AddField(
            model_name='probe',
            name='series',
            field=models.ForeignKey(related_name='probes', verbose_name=b'series', to='charts.Series'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chart',
            name='series',
            field=models.ManyToManyField(related_name='chart', verbose_name=b'series', to='charts.Series'),
            preserve_default=True,
        ),
    ]
