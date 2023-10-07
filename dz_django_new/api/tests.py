from django.test import TestCase, Client
from api.models import ApiUser, Storage, Good


class YourModelTests(TestCase):
    def setUp(self):
        self.user1 = ApiUser.objects.create_user(username='TestUser1', password='123123',
                                                 email="parshyn4@gmail.com", choice="C")
        self.user2 = ApiUser.objects.create_user(username='TestUser2', password='123123',
                                                 email="parshyn9@gmail.com", choice="P")
        self.storage = Storage.objects.create(name='TestStorage', goods={"good1": 120})
        self.good = Good.objects.create(name="TestGood")
        self.client = Client()

    def test_index_storage(self):
        response = self.client.get("/storage/")
        self.assertEqual(response.status_code, 200)

    def test_index_good(self):
        response = self.client.get("/good/")
        self.assertEqual(response.status_code, 200)

    def test_index_users(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200)

    def test_model_good_id(self):
        response = self.client.get(f'/good/{1}/')
        self.assertEqual(response.data['name'], 'TestGood')

    def test_model_storage_id(self):
        response = self.client.get(f'/storage/{1}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'TestStorage')
        self.assertEqual(response.data['goods'], {"good1": 120})

    def test_index_fromStorage(self):
        response = self.client.get(f'/storage/{1}/fromstorage/')
        self.assertEqual(response.status_code, 405)

    def test_index_ToStorage(self):
        response = self.client.get(f'/storage/{1}/tostorage/')
        self.assertEqual(response.status_code, 405)

    def test_index_ToStorage_put_not_authorized(self):
        url = f'/storage/{1}/tostorage/'
        response = self.client.post(url, good='good2', quantity=190)
        self.assertEqual(response.status_code, 401)

    def test_index_FromStorage_put_not_authorized(self):
        url = f'/storage/{1}/fromstorage/'
        response = self.client.post(url, good='good2', quantity=190)
        self.assertEqual(response.status_code, 401)

    def test_index_fromStorage_put_authorized(self):
        url = f'/storage/{1}/fromstorage/'
        self.client.login(username='TestUser2', password='123123')
        response = self.client.post(url, data={"good": "good2", "quantity": 190})
        self.assertEqual(response.status_code, 403)

    def test_index_toStorage_put_authorized(self):
        url = f'/storage/{1}/tostorage/'
        self.client.login(username='TestUser1', password='123123')
        response = self.client.post(url, data={"good": "good2", "quantity": 190})
        self.assertEqual(response.status_code, 403)
