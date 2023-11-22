from django.db import models
import uuid


class BreathalyzerTest(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    result_breathalyzer_test = models.CharField(max_length=150)
    local_breathalyzer_test = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    breathalyzerBatch = models.ForeignKey(
        "breathalyzerBatchs.BreathalyzerBatch",
        related_name="breathalyzerTests",
        on_delete=models.CASCADE, null=True
    ) 
    user = models.ForeignKey(
        "users.User",
        related_name="breathalyzerTests",
        on_delete=models.CASCADE, null=True
    ) 
    patient = models.ForeignKey(
        "patients.Patient",
        related_name="breathalyzerTests",
        on_delete=models.CASCADE, null=True
    ) 
    def __repr__(self) -> str:
        return f"<BreathalyzerTests ({self.id}) - {self.result_breathalyzer_test}>"
