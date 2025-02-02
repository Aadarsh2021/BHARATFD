from django.test import TestCase
from faq.models import FAQ
from faq.serializers import FAQSerializer

class FAQSerializerTest(TestCase):
    def setUp(self):
        """Set up test data"""
        self.faq_data = {
            "question": "What is Django?",
            "answer": "A Python web framework."
        }
        self.faq = FAQ.objects.create(**self.faq_data)

    def test_serializer_fields(self):
        """Test if serializer correctly serializes FAQ"""
        serialized_data = FAQSerializer(self.faq).data
        self.assertEqual(serialized_data["question"], "What is Django?")
        self.assertEqual(serialized_data["answer"], "A Python web framework.")

    def test_serializer_validation(self):
        """Test serializer validation for empty fields"""
        invalid_data = {"question": "", "answer": ""}
        serializer = FAQSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("question", serializer.errors)
        self.assertIn("answer", serializer.errors)  # Now correctly checks for answer validation
