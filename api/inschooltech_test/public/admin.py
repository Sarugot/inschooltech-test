from django.contrib import admin

from . import models


@admin.register(models.Lab)
class LabAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'is_active', 'created_at', 'updated_at'
        )


@admin.register(models.Test)
class TestAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'started_at', 'completed_at', 'comment', 'lab_id',
        'is_active', 'created_at', 'updated_at'
        )
