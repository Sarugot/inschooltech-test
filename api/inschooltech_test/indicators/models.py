import uuid

from django.db import models

from public.models import Test


class Indicator(models.Model):
    """Модель индикаторов"""
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='Описание',
        null=True
    )
    is_active = models.BooleanField()
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Время обновления',
        auto_now=True
    )

    class Meta:
        db_table = u'"indicators\".\"indicators"'
        verbose_name = 'Индикатор'
        verbose_name_plural = 'Индикаторы'

    def __str__(self):
        return self.name


class Metric(models.Model):
    """Модель индикаторов"""
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='Описание',
        null=True
    )
    unit = models.CharField(
        max_length=200,
        verbose_name='Единица измерения'
    )
    is_active = models.BooleanField()
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Время обновления',
        auto_now=True
    )

    class Meta:
        db_table = u'"indicators\".\"metrics"'
        verbose_name = 'Метрика'
        verbose_name_plural = 'Метрики'

    def __str__(self):
        return self.name


class Indicator_Metric(models.Model):
    """Модель индикаторов метрик"""
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True
    )
    indicator_id = models.ForeignKey(
        Indicator,
        on_delete=models.CASCADE,
        related_name='metrics',
    )
    metric_id = models.ForeignKey(
        Metric,
        on_delete=models.CASCADE,
        related_name='indicators',
    )
    is_active = models.BooleanField()
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Время обновления',
        auto_now=True
    )

    class Meta:
        db_table = u'"indicators\".\"indicators_metrics"'
        verbose_name = 'Показатель метрики'
        verbose_name_plural = 'Показатели метрик'

    def __str__(self):
        return str(self.id)


class Score(models.Model):
    """Модель результата."""
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True
    )
    score = models.DecimalField(max_digits=9, decimal_places=2)
    test_id = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='scores',
    )
    indicator_metric_id = models.ForeignKey(
        Indicator_Metric,
        on_delete=models.CASCADE,
        related_name='scores',
    )
    is_active = models.BooleanField()
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Время обновления',
        auto_now=True
    )

    class Meta:
        db_table = u'"indicators\".\"scores"'
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
        constraints = [
            models.UniqueConstraint(
                fields=['test_id', 'indicator_metric_id'],
                name='unique_test_indicator_metric'
            )
        ]

    def __str__(self):
        return str(self.id)


class Reference(models.Model):
    """Модель результата."""
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True
    )
    min_score = models.DecimalField(max_digits=9, decimal_places=2)
    max_score = models.DecimalField(max_digits=9, decimal_places=2)
    indicator_metric_id = models.OneToOneField(
        Indicator_Metric,
        on_delete=models.CASCADE,
        related_name='reference',
    )
    is_active = models.BooleanField()
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Время обновления',
        auto_now=True
    )

    class Meta:
        db_table = u'"indicators\".\"references"'
        verbose_name = 'Референсное значение'
        verbose_name_plural = 'Референсные значения'

    def __str__(self):
        return str(self.id)
