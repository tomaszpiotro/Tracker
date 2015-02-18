from django.test.testcases import TestCase

from charts.models import Chart

import autofixture


class ChartTest(TestCase):
    def setUp(self):
        self.title = "title"
        autofixture.create_one(Chart, field_values={'title': self.title,
                                                    'slug': self.title})

    def test_simple_chart_detail_view(self):
        url = '/charts/' + self.title + "/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='chart.html')

    def test_chart_detail_view_with_hours(self):
        url = '/charts/' + self.title + "/24"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='chart.html')
