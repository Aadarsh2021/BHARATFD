from django.test import TestCase
from faq.models import FAQ
from faq.serializers import FAQSerializer

class FAQSerializerTest(TestCase):
    def setUp(self):
        self.faq_data = {
            "question": "What is Django?",
            "answer": "<p>A Python web framework.</p>"
        }
        self.faq = FAQ.objects.create(**self.faq_data)

    def test_serializer_fields(self):
        """Test if serializer correctly serializes FAQ"""
        serialized_data = FAQSerializer(self.faq).data
        self.assertEqual(serialized_data["question"], "What is Django?")
        self.assertEqual(serialized_data["answer"], "<p>A Python web framework.</p>")  # Ensure rich text format is covered

    def test_serializer_with_missing_fields(self):
        """Test serializer with missing required fields"""
        invalid_data = {"answer": "<p>Only answer provided</p>"}
        serializer = FAQSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("question", serializer.errors)

    def test_serializer_validation(self):
        """Test serializer validation for empty fields"""
        invalid_data = {"question": "", "answer": ""}
        serializer = FAQSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("question", serializer.errors)
        self.assertIn("answer", serializer.errors)
        
    def test_empty_question_validation(self):
        """Ensure empty question raises a validation error"""
        invalid_data = {"question": " ", "answer": "<p>Valid answer</p>"}
        serializer = FAQSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("question", serializer.errors)


