from rest_framework.test import APIClient, APITestCase

from users.models import User


class URLTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='testowy', password='test'
            )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_url_not_available_to_anonimous_user(self):
        """Страница /results/ не доступна не авторизованному пользователю."""
        self.client.logout()
        response = self.client.get('/api/results/')
        self.assertEqual(response.status_code, 401)

    def test_url_available_to_user(self):
        """Страница /results/ доступна авторизованному пользователю."""
        response = self.client.get('/api/results/')
        self.assertEqual(response.status_code, 200)
