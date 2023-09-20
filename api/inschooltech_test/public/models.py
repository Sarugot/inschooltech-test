import uuid

from django.db import models


class Lab(models.Model):
    """Модель лабораторий"""
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
        db_table = u'"public\".\"labs"'
        verbose_name = 'Лаборатория'
        verbose_name_plural = 'Лаборатории'

    def __str__(self):
        return self.name


class Test(models.Model):
    """Модель тестов"""
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True
    )
    started_at = models.DateTimeField(
        verbose_name='Время начала тестирования',
    )
    completed_at = models.DateTimeField(
        verbose_name='Время окончания тестирования',
        null=True,
        blank=True
    )
    comment = models.CharField(
        max_length=200,
        verbose_name='Комментарий',
        null=True
    )
    lab_id = models.ForeignKey(
        Lab,
        on_delete=models.SET_NULL,
        null=True,
        related_name='tests',
        verbose_name='ID лаборатории'
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
        db_table = u'"public\".\"tests"'
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return str(self.id)
