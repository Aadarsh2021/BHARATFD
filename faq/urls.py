from django.urls import path
from .views import FAQListView  # Import your views

urlpatterns = [
    path('faqs/', FAQListView.as_view(), name='faq-list'),  # No 'admin/' here
]
