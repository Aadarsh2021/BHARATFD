import pytest
from faq.models import FAQ
from faq.serializers import FAQSerializer
from django.utils.html import strip_tags


@pytest.mark.django_db
class FAQSerializerTest:
    def setup_method(self):
        """Set up test data"""
        self.faq_data = {
            "question": "What is Django?",
            "answer": "<p>A Python web framework.</p>",
        }

    def test_serializer_fields(self):
        """Test if serializer correctly serializes FAQ"""
        faq = FAQ.objects.create(**self.faq_data)
        serialized_data = FAQSerializer(faq).data
        assert serialized_data["question"] == "What is Django?"
        assert strip_tags(serialized_data["answer"]) == "A Python web framework."
