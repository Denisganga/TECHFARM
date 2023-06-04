from django import forms
from .models import Crops

class CropsForm(forms.ModelForm):
    class Meta:
        model=Crops
        fields="__all__"