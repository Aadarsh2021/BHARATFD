from django.test import TestCase  # ✅ This was missing!
from rest_framework.test import APIClient
from faq.models import FAQ

class FAQAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faq = FAQ.objects.create(
            question="What is Django?", answer="A Python web framework.",
            question_hi="Django क्या है?", answer_hi="Django एक पायथन वेब फ्रेमवर्क है।"
        )

    def test_get_faqs(self):
        """Test API returns FAQ list"""
        response = self.client.get("/api/faqs/")
        self.assertEqual(response.status_code, 200)

    def test_get_faqs_in_hindi(self):
        """Test API returns translated FAQs in Hindi"""
        response = self.client.get("/api/faqs/?lang=hi")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["question"], "Django क्या है?")
        self.assertEqual(response.json()[0]["answer"], "Django एक पायथन वेब फ्रेमवर्क है।")
