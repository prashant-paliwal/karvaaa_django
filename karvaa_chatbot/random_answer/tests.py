from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from scipy.stats import chisquare
from .responses import random_sentences

print(random_sentences)
class ChatbotAnswerTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_chatbot_response(self):
        url = reverse('chatbot_response')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.client.get(url).json(), random_sentences)

    def test_response_randomness(self):
        # Testing randomness using 1000 sample values
        url = reverse('chatbot_response')
        responses = [self.client.get(url).json() for _ in range(1000)]
        counts = [responses.count(response) for response in set(responses)]
        chi2, p_value = chisquare(counts)
        self.assertGreater(p_value, 0.05)
