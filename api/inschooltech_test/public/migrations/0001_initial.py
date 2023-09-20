# Generated by Django 4.2.5 on 2023-09-19 19:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('is_active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
            ],
            options={
                'verbose_name': 'Лаборатория',
                'verbose_name_plural': 'Лаборатории',
                'db_table': '"public"."labs"',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('started_at', models.DateTimeField(verbose_name='Время начала тестирования')),
                ('completed_at', models.DateTimeField(blank=True, null=True, verbose_name='Время окончания тестирования')),
                ('comment', models.CharField(max_length=200, null=True, verbose_name='Комментарий')),
                ('is_active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('lab_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tests', to='public.lab', verbose_name='ID лаборатории')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
                'db_table': '"public"."tests"',
            },
        ),
    ]
