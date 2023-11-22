from django.db.models.signals import post_migrate
from django.dispatch import receiver
from users.models import User
from clients.models import Client


@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    client = Client.objects.filter(client_name = "FRB").first()
    
    if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                name='Admin',
                username='admin@admin.com',
                email='admin@admin.com',
                password='admin@admin.com',
                user_level='admin',
                client= client
            )