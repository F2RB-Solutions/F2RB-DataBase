# Generated by Django 4.2.1 on 2023-11-15 18:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("quizs", "0003_alter_quiz_patients_alter_quiz_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="quiz",
            old_name="patients",
            new_name="patient",
        ),
    ]
