from django.views.generic.detail import DetailView

from charts.models import Chart


class ChartDetailView(DetailView):
    model = Chart
    template_name = "chart.html"

    def get_queryset(self):
        return Chart.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, hours=48, **kwargs):
        if 'hours' in self.kwargs:
            hours = int(self.kwargs['hours'])
        context = super(ChartDetailView, self).get_context_data(**kwargs)
        chart = context['chart']
        context['chart_id'] = 'chart'
        context['type'] = chart.type
        context['title'] = chart.title
        context['xAxis'] = chart.x_axis_name
        context['yAxis'] = chart.y_axis_name
        context['series'] = chart.get_chart_json(hours=hours)
        return context
