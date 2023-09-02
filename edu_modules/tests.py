from rest_framework.test import APITestCase
from rest_framework import status
from edu_modules.models import Module
from users.models import User, UserRoles


class ModuleTestCase(APITestCase):
    """Тесты модели Module"""
    def setUp(self) -> None:
        """Подготовка данных перед тестом"""
        self.user = User.objects.create(
            email='user@user.com',
            is_staff=False,
            is_superuser=False,
            is_active=True,
            role=UserRoles.MEMBER,
        )
        self.user.set_password('123')
        self.user.save()
        response = self.client.post('/api/token/', {"email": "user@user.com", "password": "123"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_model_name = 'module_for_test'

    def test_module_create(self):
        """Тест создания модели Module"""
        response = self.client.post('/api/edu_modules/', {'number': 1, 'name': self.test_model_name})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_module(self):
        """Тест деталей модели Module"""
        self.test_module_create()
        response = self.client.get('/api/edu_modules/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['id'], 1)

    def test_list_module(self):
        """Тест списка модели Module"""
        self.test_module_create()
        response = self.client.get('/api/edu_modules/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Module.objects.all().count(), 1)

    def test_module_update_view(self):
        self.test_module_create()
        response_update = self.client.patch('/api/edu_modules/5/', {"name": "Урок 5"})
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(response_update.json()['name'], 'Урок 5')

    def test_module_deletion_view(self):
        self.test_module_create()
        response = self.client.delete('/api/edu_modules/4/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Module.objects.filter(id=1).exists())
