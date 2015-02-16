from django.test.testcases import TestCase
from charts.models import Chart

import autofixture


class ChartTest(TestCase):
    def test_simple_chart_detail_view(self):
        title = "title"
        autofixture.create_one(Chart, field_values={'title': title,
                                                    'slug': title})
        url = '/charts/' + title + "/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='chart.html')
