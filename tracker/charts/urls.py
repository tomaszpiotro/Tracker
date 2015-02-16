from django.conf.urls import patterns, url
from charts.views import ChartDetailView

urlpatterns = patterns(
    'charts.views',
    url(r'(?P<slug>[-\w]*)/$', ChartDetailView.as_view()),
)
