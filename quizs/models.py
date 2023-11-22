from django.db import models
import uuid


class Quiz(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    regular_medication = models.BooleanField()
    description_regular_medication= models.CharField(null=True,max_length=150)
    consumed_alcoholic = models.BooleanField()
    description_consumed_alcoholic = models.CharField(null=True, max_length=150)
    consumed_drugs = models.BooleanField()
    description_consumed_drugs = models.CharField(null=True,max_length=150) 
    result = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    user = models.ForeignKey(
        "users.User",
        related_name="quizs",
        on_delete=models.CASCADE, null=True
    )    
    patient = models.ForeignKey(
        "patients.Patient",
        related_name="quizs",
        on_delete=models.CASCADE, null=True
    )    
    def __repr__(self) -> str:
        return f"<Quiz ({self.id}) - {self.regular_medication}>"
