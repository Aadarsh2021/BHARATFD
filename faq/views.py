from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ


class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get("lang", "en")  # Default to English
        faqs = FAQ.objects.all()
        data = [faq.get_translation(lang) for faq in faqs]
        return Response(data)
