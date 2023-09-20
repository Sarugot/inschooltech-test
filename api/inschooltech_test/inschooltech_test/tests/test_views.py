from datetime import datetime
from rest_framework.test import APIClient, APITestCase

from indicators.models import (
    Indicator, Metric, Indicator_Metric, Score, Reference
    )
from public.models import Lab, Test
from users.models import User
from indicators.serializers import TestSerializer


class SnippetsList(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_superuser(
            username='testowy',
            password='test'
            )
        cls.lab = Lab.objects.create(
            name='Имя лаборатории',
            is_active=True
        )
        cls.test = Test.objects.create(
            lab_id=cls.lab,
            is_active=True,
            started_at=datetime.now(),
            completed_at=datetime.now()
        )
        cls.indicator = Indicator.objects.create(
            name='Имя индикатора',
            is_active=True
        )
        cls.metric = Metric.objects.create(
            name='Имя метрики',
            unit='Название единицы измерения',
            is_active=True
        )
        cls.indicator_metric = Indicator_Metric.objects.create(
            indicator_id=cls.indicator,
            metric_id=cls.metric,
            is_active=True
        )
        cls.score = Score.objects.create(
            score=10,
            test_id=cls.test,
            indicator_metric_id=cls.indicator_metric,
            is_active=True
        )
        cls.reference = Reference.objects.create(
            min_score=5,
            max_score=20,
            indicator_metric_id=cls.indicator_metric,
            is_active=True
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_api_data(self):
        """Проверка соответствия даты API."""
        response = self.client.get('/api/results/')
        queryset = Test.objects.filter(
            is_active=True, completed_at__isnull=False
            )
        serializer = TestSerializer(queryset, many=True)
        self.assertEqual(
            response.data, serializer.data
            )
