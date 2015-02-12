from django.conf.urls import patterns, url
from charts.views import ChartDetailView

urlpatterns = patterns(
    'charts.views',
    url(r'(?P<pk>\d+)', ChartDetailView.as_view()),
)
