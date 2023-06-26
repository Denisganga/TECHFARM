from django import forms
from .models import Reports

class ReportsForm(forms.ModelForm):
    class Meta:
        model=Reports
        fields=['Rid','date','the_field','the_report']