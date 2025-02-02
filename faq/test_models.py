from django.test import TestCase
from .models import FAQ


class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?", answer="Django is a Python web framework."
        )

    def test_faq_creation(self):
        """Test if FAQ is created successfully."""
        self.assertEqual(self.faq.question, "What is Django?")
        self.assertEqual(self.faq.answer, "Django is a Python web framework.")


class FAQAPITest(TestCase):
    def test_get_faqs(self):
        """Test if API returns FAQs"""
        response = self.client.get("/api/faqs/")
        self.assertEqual(response.status_code, 200)
