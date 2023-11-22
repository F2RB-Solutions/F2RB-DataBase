from django.db import models
import uuid


class BreathalyzerBatch(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    surname_breathalyzer = models.CharField(max_length=150, unique=True)
    serial_number_breathalyzer = models.CharField(max_length=150)
    certificate_number_breathalyzer = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
   
    def __repr__(self) -> str:
        return f"<BreathalyzerBatch ({self.id}) - {self.surname_breathalyzer}>"
