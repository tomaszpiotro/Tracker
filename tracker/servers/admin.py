from django.contrib import admin
from .models import HttpSeries


@admin.register(HttpSeries)
class HttpSeries(admin.ModelAdmin):
    list_display = ['url', 'name', 'tag', 'html_id', 'html_class']
