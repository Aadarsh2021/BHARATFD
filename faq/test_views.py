from django.test import TestCase
from rest_framework.test import APIClient
from .models import FAQ

class FAQAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        FAQ.objects.create(question="What is Django?", answer="A web framework.")

    def test_get_faqs(self):
        """Test API returns FAQ list"""
        response = self.client.get("/api/faqs/")
        self.assertEqual(response.status_code, 200)
