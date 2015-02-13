from django.views.generic.detail import DetailView
from charts.models import Chart


class ChartDetailView(DetailView):
    model = Chart
    template_name = "chart.html"

    def get_context_data(self, **kwargs):
        context = super(ChartDetailView, self).get_context_data(**kwargs)
        chart = context['chart']
        context['chart_id'] = "'chart'"
        context['type'] = "'line'"
        context['title'] = "'" + str(chart.title) + "'"
        context['xAxis'] = "'X'"
        context['yAxis'] = "'Y'"
        context['series'] = \
            "[" \
            + "{name: 'total', data: " \
            + chart.get_data('total') + ", color: 'grey' }" \
            + ",{ name: 'alliance', data: " \
            + chart.get_data('alliance') + ", color: 'blue'}" \
            + ",{ name: 'horde', data: " \
            + chart.get_data("horde") + ", color: 'red' }" \
            + "]"

        return context
