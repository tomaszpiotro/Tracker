from django.db import models


class Probe(models.Model):
    datetime = models.DateTimeField(
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
        app_label = "wow_charts"


class Series(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name="name"
    )

    class Meta:
        app_label = "wow_charts"


class Chart(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name="title"
    )
    series = models.ManyToManyField(
        Series,
        verbose_name="series"
    )
