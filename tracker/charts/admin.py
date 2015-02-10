from django.contrib import admin
from charts.models import Probe


@admin.register(Probe)
class HttpSeries(admin.ModelAdmin):
    list_display = ['date', 'value', 'series']
