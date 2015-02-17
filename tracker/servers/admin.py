from django.contrib import admin
from .models import HttpSeries
from servers.models import NestedSeries, ThirdNextSibling


@admin.register(HttpSeries)
class HttpSeries(admin.ModelAdmin):
    list_display = ['url', 'name', 'tag', 'html_id', 'html_class']


@admin.register(NestedSeries)
class NestedSeriesAdmin(HttpSeries):
    pass


@admin.register(ThirdNextSibling)
class NestedSeriesAdmin(HttpSeries):
    pass
