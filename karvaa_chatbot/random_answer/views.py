from django.http import JsonResponse
from rest_framework.views import APIView
import random

from .responses import random_sentences


class ChatbotResponse(APIView):
    def get(self, request):
        response = random.choice(random_sentences)
        return JsonResponse(response, safe=False)
