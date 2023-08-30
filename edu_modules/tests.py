from rest_framework.test import APITestCase
from rest_framework import status
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
        response = self.client.post('/api/edu_modules/', {'name': self.test_model_name})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_habit(self):
        """Тест деталей модели Module"""
        self.test_module_create()
        response = self.client.get(f'/api/edu_modules/1/')
        print(response.json()['id'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['id'], 1)
