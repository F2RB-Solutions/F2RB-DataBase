# Generated by Django 4.2.1 on 2024-01-10 20:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("quizs", "0006_alter_quiz_description_consumed_alcoholic_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quiz",
            name="description_consumed_alcoholic",
        ),
    ]
