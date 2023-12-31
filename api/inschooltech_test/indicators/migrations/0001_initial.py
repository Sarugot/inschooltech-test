# Generated by Django 4.2.5 on 2023-09-19 19:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='Описание')),
                ('is_active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
            ],
            options={
                'verbose_name': 'Индикатор',
                'verbose_name_plural': 'Индикаторы',
                'db_table': '"indicators"."indicators"',
            },
        ),
        migrations.CreateModel(
            name='Indicator_Metric',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('is_active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('indicator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metrics', to='indicators.indicator')),
            ],
            options={
                'verbose_name': 'Показатель метрики',
                'verbose_name_plural': 'Показатели метрик',
                'db_table': '"indicators"."indicators_metrics"',
            },
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='Описание')),
                ('unit', models.CharField(max_length=200, verbose_name='Единица измерения')),
                ('is_active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
            ],
            options={
                'verbose_name': 'Метрика',
                'verbose_name_plural': 'Метрики',
                'db_table': '"indicators"."metrics"',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('score', models.DecimalField(decimal_places=2, max_digits=9)),
                ('is_active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('indicator_metric_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='indicators.indicator_metric')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='public.test')),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
                'db_table': '"indicators"."scores"',
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('min_score', models.DecimalField(decimal_places=2, max_digits=9)),
                ('max_score', models.DecimalField(decimal_places=2, max_digits=9)),
                ('is_active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('indicator_metric_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reference', to='indicators.indicator_metric')),
            ],
            options={
                'verbose_name': 'Референсное значение',
                'verbose_name_plural': 'Референсные значения',
                'db_table': '"indicators"."references"',
            },
        ),
        migrations.AddField(
            model_name='indicator_metric',
            name='metric_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indicators', to='indicators.metric'),
        ),
        migrations.AddConstraint(
            model_name='score',
            constraint=models.UniqueConstraint(fields=('test_id', 'indicator_metric_id'), name='unique_test_indicator_metric'),
        ),
    ]
