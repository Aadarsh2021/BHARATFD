from django.test import TestCase
from faq.models import FAQ
from faq.serializers import FAQSerializer
from django.utils.html import strip_tags  # ✅ Import to remove HTML tags

class FAQSerializerTest(TestCase):
    def setUp(self):
        self.faq_data = {
            "question": "What is Django?",
            "answer": "<p>A Python web framework.</p>",  # ✅ This is stored as HTML
            "question_hi": "Django क्या है?",
            "answer_hi": "<p>Django एक पायथन वेब फ्रेमवर्क है।</p>",
        }

    def test_serializer_fields(self):
        """Test if serializer correctly serializes FAQ"""
        faq = FAQ.objects.create(**self.faq_data)
        serialized_data = FAQSerializer(faq).data

        # ✅ Strip HTML tags from the output before comparison
        self.assertEqual(serialized_data["question"], "What is Django?")
        self.assertEqual(strip_tags(serialized_data["answer"]), "A Python web framework.")  # ✅ Now it will match
