# Generated by Django 4.2.1 on 2023-11-14 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0002_alter_client_client_email_and_more"),
        ("users", "0002_user_coren_user_cpf_user_tel_alter_user_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="client",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to="clients.client",
            ),
        ),
    ]
