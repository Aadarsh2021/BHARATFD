from rest_framework import serializers
from .models import FAQ
from bs4 import BeautifulSoup


class FAQSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()

    def get_answer(self, obj):
        return (
            f"<p>{obj.answer}</p>" if not obj.answer.startswith("<p>") else obj.answer
        )

    class Meta:
        model = FAQ
        fields = "__all__"


def get_answer(self, obj):
    return BeautifulSoup(obj.answer, "html.parser").text  # Removes HTML
