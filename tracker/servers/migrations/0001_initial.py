# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HttpSeries',
            fields=[
                ('series_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='charts.Series')),
                ('url', models.URLField(verbose_name=b'url')),
                ('tag', models.CharField(max_length=32, null=True, verbose_name=b'tag')),
                ('html_id', models.CharField(max_length=64, null=True, verbose_name=b'id')),
                ('html_class', models.CharField(max_length=64, null=True, verbose_name=b'id')),
            ],
            options={
                'abstract': False,
            },
            bases=('charts.series', models.Model),
        ),
        migrations.CreateModel(
            name='Realm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name=b'realm name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name=b'server name')),
                ('website_address', models.URLField(verbose_name=b'website address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='realm',
            name='server',
            field=models.ForeignKey(related_name='realms', verbose_name=b'server', to='servers.Server'),
            preserve_default=True,
        ),
    ]
