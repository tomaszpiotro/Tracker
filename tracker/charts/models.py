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

    def get_data(self, series_name):
        result = "["
        for probe in self.series.get(name=series_name).probes.all():
            date = (str(probe.date.year) + ", " + str(probe.date.month - 1)
                    + ", " + str(probe.date.day) + ", " + str(probe.date.hour)
                    + ", " + str(probe.date.minute) + ", "
                    + str(probe.date.second))
            date = "Date.UTC(" + str(date) + ")"
            res = "[" + date + ", " + str(probe.value) + "], "
            result += res
        result += "]"
        return result
