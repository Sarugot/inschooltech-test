from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from public.models import Test
from .serializers import TestSerializer


class ResultsView(ListAPIView):
    queryset = Test.objects.filter(
            is_active=True, completed_at__isnull=False
            )
    serializer_class = TestSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('lab_id',)
