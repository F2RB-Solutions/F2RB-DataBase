# Generated by Django 4.2.1 on 2024-01-10 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("pressureMonitorBatchs", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("patients", "0003_alter_patient_client"),
    ]

    operations = [
        migrations.CreateModel(
            name="PressureMonitor",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("local_pressure_monitor_test", models.CharField(max_length=150)),
                ("measuring_blood_repressure_test", models.CharField(max_length=150)),
                ("result_pressure_monitor_test", models.CharField(max_length=150)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "patient",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pressureMonitors",
                        to="patients.patient",
                    ),
                ),
                (
                    "pressureMonitorBatch",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pressureMonitors",
                        to="pressureMonitorBatchs.pressuremonitorbatch",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pressureMonitors",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]