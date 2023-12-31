from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from indicators.models import Score
from public.models import Test
from users.models import User


class CustomUserCreateSerializer(UserCreateSerializer):
    """Видоизменённый сериализатор создания пользователя djoser."""
    class Meta:
        model = User
        fields = (
            'email', 'id', 'username', 'password',
        )


class CustomUserSerializer(UserSerializer):
    """Видоизменённый сериализатор пользователя djoser."""

    class Meta:
        model = User
        fields = (
            'id', 'email', 'username'
        )

    def get_is_subscribed(self, obj):
        user = self.context.get('request').user
        return user.is_authenticated and user.followers.filter(
            author=obj.id
        ).exists()


class ScoresSerializer(serializers.ModelSerializer):
    """Сериализатор для выведения данных подписок пользователя."""
    indicator_name = serializers.ReadOnlyField(
        source='indicator_metric_id.indicator_id.name'
        )
    metric_name = serializers.ReadOnlyField(
        source='indicator_metric_id.metric_id.name'
        )
    metric_unit = serializers.ReadOnlyField(
        source='indicator_metric_id.metric_id.unit'
        )
    is_within_normal_range = serializers.SerializerMethodField()

    class Meta:
        model = Score
        fields = ('id', 'score', 'indicator_name', 'metric_name',
                  'metric_unit', 'is_within_normal_range')

    def get_is_within_normal_range(self, obj):
        return (obj.indicator_metric_id.reference.min_score <=
                obj.score <=
                obj.indicator_metric_id.reference.max_score)


class TestSerializer(serializers.ModelSerializer):
    """Сериализатор для выведения данных подписок пользователя."""
    duration_seconds = serializers.SerializerMethodField()
    results = ScoresSerializer(many=True, source='scores')

    class Meta:
        model = Test
        fields = ('id', 'lab_id', 'duration_seconds', 'results')

    def get_duration_seconds(self, obj):
        return obj.completed_at - obj.started_at
