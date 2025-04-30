from django.db import models

# Create your models here.
from django.db import models

# Model to store personal information
class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)  # Name of the user
    reg_number = models.CharField(max_length=50)  # Registration number or ID
    occupation = models.CharField(max_length=100)  # Occupation of the user
    gender = models.CharField(max_length=10)  # Gender (Male or Female)
    security_question_answer = models.CharField(max_length=50)  # Answer to the security question

    def __str__(self):
        return self.name  # This will return the name when printing a PersonalInfo object


# Model to store budgeting information
class Budget(models.Model):
    user = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)  # Link budget to personal info
    initial_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Initial budget amount
    duration_days = models.IntegerField()  # Number of days for the budget
    last_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Last amount remaining in the budget
    created_at = models.DateTimeField(auto_now_add=True)  # Date when the budget was created

    def __str__(self):
        return f"Budget for {self.user.name} - KSh {self.initial_amount}"  # Displays user and budget amount
