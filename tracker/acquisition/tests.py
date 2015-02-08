from django.test import TestCase
from .models import Acquisition


class AcquisitionTest(TestCase):
    def setUp(self):
        self.html_class, self.html_id = 'cls', 'some-id'
        self.acquisition = Acquisition(html_class=self.html_class,
                                       html_id=self.html_id)

    def test_simple_prepare_attributes(self):
        tested_dict = self.acquisition._prepare_attributes()
        self.assertDictContainsSubset(expected={'class': self.html_class,
                                                'id': self.html_id},
                                      actual=tested_dict)

    def test_one_value_prepare_attributes(self):
        self.acquisition.html_class = None
        tested_dict = self.acquisition._prepare_attributes()
        self.assertDictContainsSubset(expected={'id': self.html_id},
                                      actual=tested_dict)
        self.assertNotIn('class', tested_dict)

    def test_empty_prepare_attributes(self):
        self.acquisition.html_id, self.acquisition.html_class = None, None
        tested_dict = self.acquisition._prepare_attributes()
        self.assertDictEqual(tested_dict, {})
