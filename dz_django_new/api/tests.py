import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import ApiUser, Storage, Good

class YourModelTests(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = ApiUser.objects.create_user(username='testuser', password='testpass')

        # Создаем тестовый объект YourModel
        self.your_model = Storage.objects.create(name='TestObject', user=self.user)

        # Создаем клиента API
        self.client = APIClient()

    def test_get_your_model(self):
        # Получаем тестовый объект YourModel через API
        response = self.client.get(f'/storage/{self.your_model.id}/')

        # Проверяем, что запрос был успешным (HTTP статус 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что данные объекта совпадают с ожидаемыми
        self.assertEqual(response.data['name'], 'TestObject')
        self.assertEqual(response.data['user'], self.user.id)