from django import forms
from .models import Crops

class CropsForm(forms.ModelForm):
    class Meta:
        model=Crops
        fields=['cid','name','variety','planting_date','description','quantity','is_harvested']