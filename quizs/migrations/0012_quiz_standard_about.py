# Generated by Django 4.1.7 on 2024-01-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quizs", "0011_quiz_prefer_alters_ability_activities_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="quiz",
            name="standard_about",
            field=models.CharField(max_length=150, null=True),
        ),
    ]
