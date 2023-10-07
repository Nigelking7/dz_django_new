from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from api.models import ApiUser, Storage


class YourModelTests(TestCase):
    def setUp(self):
        self.user = ApiUser.objects.create_user(username='testuser', password='testpass')
        self.your_model = Storage.objects.create(name='TestObject', user=self.user)
        self.client = APIClient()

    def test_get_your_model(self):
        response = self.client.get(f'/storage/{self.your_model.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'TestObject')
        self.assertEqual(response.data['user'], self.user.id)
