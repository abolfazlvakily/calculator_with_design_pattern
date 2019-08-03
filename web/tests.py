from django.test import TestCase
from django.urls import reverse


class UnitTest(TestCase):
    def test_sum(self):
        # sum two numbers
        url = reverse('web:sum', kwargs={'first_number': 1, 'second_number': 2})
        response = self.client.get(url)
        self.assertEqual(response.context['sum'], 3)

    def test_subtracion(self):
        # subtraction two numbers
        url = reverse('web:subtraction', kwargs={'first_number': 8, 'second_number': 2})
        response = self.client.get(url)
        self.assertEqual(response.context['subtraction'], 6)


class IntegrationTest(TestCase):
    pass


class EndToEndTest(TestCase):
    pass
