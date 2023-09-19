from django.contrib import admin

from . import models


@admin.register(models.Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description', 'is_active', 'created_at', 'updated_at'
        )


@admin.register(models.Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description', 'unit',
        'is_active', 'created_at', 'updated_at'
        )


@admin.register(models.Indicator_Metric)
class Indicator_MetricAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'indicator_id', 'metric_id',
        'is_active', 'created_at', 'updated_at'
        )


@admin.register(models.Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'score', 'test_id', 'indicator_metric_id',
        'is_active', 'created_at', 'updated_at'
        )


@admin.register(models.Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'min_score', 'max_score', 'indicator_metric_id',
        'is_active', 'created_at', 'updated_at'
        )
