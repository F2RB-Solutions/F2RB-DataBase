from django.db import models
import uuid


class Patient(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    role = models.CharField(null=True, max_length=255)
    date_birth = models.CharField(null=True, max_length=10)
    email = models.EmailField(null=True, unique=True)
    tel = models.CharField(null=True,max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    client = models.ForeignKey(
        "clients.Client",
        related_name="patients",
        on_delete=models.CASCADE, null=True
    )    
   
    def __repr__(self) -> str:
        return f"<Patient ({self.id}) - {self.username}>"
