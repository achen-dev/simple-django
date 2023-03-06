from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class APIPlaygroundViewTests(TestCase):
    def test_numbers_api(self):
        api_call = "23"
        url = reverse('blog:apiPlayground', )
        response = self.client.get(url)
        self.assertContains(response.status_code, 200)