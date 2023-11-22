from django.db import models
import uuid


class DrugTestBatch(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    surname_drug_test_batch = models.CharField(max_length=150, unique=True)
    register_drug_test_batch = models.CharField(max_length=150)
    validity_drug_test_batch = models.CharField(max_length=150)
    method_drug_test_batch = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
   
    def __repr__(self) -> str:
        return f"<DrugTestBatch ({self.id}) - {self.surname_drug_test_batch}>"
