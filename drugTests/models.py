from django.db import models
import uuid


class DrugTest(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    result_drug_test = models.CharField(max_length=150)
    local_drug_test = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    drugTestBatch = models.ForeignKey(
        "drugTestBatchs.DrugTestBatch",
        related_name="drugTests",
        on_delete=models.CASCADE, null=True
    )
    user = models.ForeignKey(
        "users.User",
        related_name="drugTests",
        on_delete=models.CASCADE, null=True
    )  
    patient = models.ForeignKey(
        "patients.Patient",
        related_name="drugTests",
        on_delete=models.CASCADE, null=True
    )    
   
    def __repr__(self) -> str:
        return f"<DrugTest ({self.id}) - {self.result_drug_test}>"
