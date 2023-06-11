from django import forms
from .models import Machinery

class MachineryForm(forms.ModelForm):
    class Meta:
        model=Machinery
        fields=['number_plate','model','purchase_date','description','manufacture_year','purchase_price']