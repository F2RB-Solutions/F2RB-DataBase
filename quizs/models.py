from django.db import models
import uuid


class Quiz(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    select_corresponding_unit = models.CharField(max_length=150)
    change_in_health = models.BooleanField()
    description_change_in_health = models.CharField(null=True,max_length=150)
    pain_moment = models.BooleanField()
    description_pain_moment = models.CharField(null=True,max_length=150)
    noticed_change_concentration = models.BooleanField()
    description_noticed_change_concentration = models.CharField(null=True,max_length=150)
    noticing_changes_sleep = models.BooleanField()
    description_noticing_changes_sleep = models.CharField(null=True,max_length=150)
    alters_ability_activities = models.BooleanField()
    description_alters_ability_activities = models.CharField(null=True,max_length=150)
    currently_locomotor_difficulties = models.BooleanField()
    description_currently_locomotor_difficulties = models.CharField(null=True,max_length=150)
    recent_changes_mood = models.BooleanField()
    description_recent_changes_mood = models.CharField(null=True,max_length=150)
    regular_medication = models.BooleanField()
    description_regular_medication= models.CharField(null=True,max_length=150)
    consumed_alcoholic = models.BooleanField()
    consumed_drugs = models.BooleanField()
    description_consumed_drugs = models.CharField(null=True,max_length=150) 
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
