from django.urls import path
from .views import ChatbotResponse
urlpatterns = [
    path('chat', ChatbotResponse.as_view(), name='chatbot_response')
]
