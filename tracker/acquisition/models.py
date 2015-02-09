from django.db import models

import requests
from bs4 import BeautifulSoup


class Acquisition(models.Model):
    url = models.URLField(
        verbose_name="url"
    )
    tag = models.CharField(
        verbose_name="tag",
        max_length=32,
        null=True
    )
    html_id = models.CharField(
        verbose_name="id",
        max_length=64,
        null=True
    )
    html_class = models.CharField(
        verbose_name="id",
        max_length=64,
        null=True
    )

    class Meta:
        abstract = True

    def get_data(self):
        request = requests.get(self.url)
        parsed = BeautifulSoup(request.content)
        value = parsed.body.find(self.tag, attrs=self._prepare_attributes())
        return value.text

    def _prepare_attributes(self):
        result = {}
        if self.html_class:
            result.update({'class': self.html_class})
        if self.html_id:
            result.update({'id': self.html_id})
        return result
