from django.contrib import admin

from .models import Probe, Chart, NestedSeries, ThirdNextSibling, HttpSeries


@admin.register(Probe)
class ProbeAdmin(admin.ModelAdmin):
    list_display = ['date', 'value', 'series']
    list_filter = ['series__name']


@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'x_axis_name', 'y_axis_name']
    filter_horizontal = ['series']


@admin.register(HttpSeries)
class HttpSeriesAdmin(admin.ModelAdmin):
    list_display = ['url', 'name', 'tag', 'html_id', 'html_class']


@admin.register(NestedSeries)
class NestedSeriesAdmin(HttpSeriesAdmin):
    pass


@admin.register(ThirdNextSibling)
class NestedSeriesAdmin(HttpSeriesAdmin):
    pass
