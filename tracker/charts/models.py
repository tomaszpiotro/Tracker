from django.db import models


class Series(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name="name"
    )

    def create_next_value(self):
        raise NotImplementedError

    def __str__(self):
        return self.name


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
