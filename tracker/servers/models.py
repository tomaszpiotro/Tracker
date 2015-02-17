from django.db import models

from charts.models import Probe, Series
from acquisition.models import Acquisition


class Server(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name="server name"
    )
    website_address = models.URLField(
        verbose_name="website address"
    )


class Realm(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name="realm name"
    )
    server = models.ForeignKey(
        Server,
        verbose_name="server",
        related_name="realms"
    )


class HttpSeries(Acquisition, Series):
    def create_next_value(self):
        probe = Probe.objects.create(value=self.get_data(), series=self)
        return probe


class NestedSeries(HttpSeries):
    def extra_process(self, value):
        return value.next


class ThirdNextSibling(NestedSeries):
    def extra_process(self, value):
        return value.find_next_sibling().find_next_sibling().next
