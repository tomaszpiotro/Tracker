from django.db import models
from django.utils import timezone

import datetime
import json
import calendar


def to_timestamp(dt):
    stamp = calendar.timegm(dt.timetuple()) * 1000
    return stamp


class Series(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name="name"
    )
    color = models.CharField(
        max_length=32,
        verbose_name="color",
        blank=True
    )

    def create_next_value(self):
        raise NotImplementedError

    def __str__(self):
        return self.name

    def get_data(self, hours=24):
        start = timezone.now() - datetime.timedelta(hours=hours)
        data = [[to_timestamp(probe.date), probe.value]
                for probe in self.probes.all().filter(date__gt=start)]
        return data


class Probe(models.Model):
    date = models.DateTimeField(
        verbose_name="datetime",
        auto_now_add=True
    )
    value = models.IntegerField(
        verbose_name="value"
    )
    series = models.ForeignKey(
        Series,
        verbose_name="series",
        related_name="probes"
    )

    class Meta:
        ordering = ['date']

    def __str__(self):
        return ", ".join([self.series.name, str(self.date), str(self.value)])


class Chart(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name="title"
    )
    series = models.ManyToManyField(
        Series,
        verbose_name="series",
        related_name="chart"
    )
    type = models.CharField(
        max_length=128,
        verbose_name="type"
    )
    x_axis_name = models.CharField(
        max_length=32,
        verbose_name="x axis name"
    )
    y_axis_name = models.CharField(
        max_length=32,
        verbose_name="y axis name"
    )

    def get_chart_json(self):
        series_list = []
        for series in self.series.all():
            single_series = {}
            single_series.update({'name': series.name,
                                  'data': series.get_data(),
                                  'color': series.color})
            series_list.append(single_series)
        return json.dumps(series_list)
