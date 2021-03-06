from django.db import models

import re
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
        null=True,
        blank=True
    )
    html_class = models.CharField(
        verbose_name="class",
        max_length=64,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

    def _get_text(self):
        request = requests.get(self.url)
        parsed = BeautifulSoup(request.content)
        value = parsed.body.find(self.tag, attrs=self._prepare_attributes())
        return value

    def extra_process(self, value):
        return value

    def get_data(self):
        value = self.extra_process(self._get_text())
        if not value.text.isdigit():
            return re.sub("[^0-9]", "", value.text)
        return value.text

    def _prepare_attributes(self):
        result = {}
        if self.html_class:
            result.update({'class': self.html_class})
        if self.html_id:
            result.update({'id': self.html_id})
        return result
