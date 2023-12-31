from django.db import models
import uuid


class Client(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    client_name = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=20, unique=True)
    corporate_name = models.CharField(max_length=150)
    tel = models.CharField(max_length=20, null=True, blank=True)
    client_email = models.EmailField(max_length=150, null=True, blank=True)
    contract_health = models.CharField(max_length=50,null=True, blank=True)
    contract_life = models.CharField(max_length=50, null=True, blank=True)
    contract_dental = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __repr__(self) -> str:
        return f"<Client ({self.id}) - {self.client_name}>"
