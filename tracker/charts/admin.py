from django.contrib import admin
from charts.models import Probe, Chart


@admin.register(Probe)
class HttpSeries(admin.ModelAdmin):
    list_display = ['date', 'value', 'series']
    list_filter = ['series__name']

@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'x_axis_name', 'y_axis_name']
    filter_horizontal = ['series']
