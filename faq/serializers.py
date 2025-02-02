from rest_framework import serializers
from faq.models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ["question", "answer"]

    def validate_question(self, value):
        """Ensure question is not empty"""
        if not value.strip():
            raise serializers.ValidationError("Question cannot be empty.")
        return value

    def validate_answer(self, value):
        """Ensure answer is not empty"""
        if not value.strip():
            raise serializers.ValidationError("Answer cannot be empty.")
        return value
