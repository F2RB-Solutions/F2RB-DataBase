# Generated by Django 4.2.1 on 2024-01-10 20:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PressureMonitorBatch",
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
                (
                    "surname_pressure_monitor",
                    models.CharField(max_length=150, unique=True),
                ),
                ("serial_number_pressure_monitor", models.CharField(max_length=150)),
                ("lote_number_pressure_monitor", models.CharField(max_length=150)),
                (
                    "certificate_number_pressure_monitor",
                    models.CharField(max_length=150),
                ),
                ("model_pressure_monitor", models.CharField(max_length=150)),
                ("brand_pressure_monitor", models.CharField(max_length=150)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
    ]
