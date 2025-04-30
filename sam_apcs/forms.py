from django import forms
from .models import PersonalInfo, Budget

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount', 'duration_in_days', 'personal_info']
