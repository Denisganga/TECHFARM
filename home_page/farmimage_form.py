from django import forms
from.models import Farmimage

class FarmimageForm(forms.ModelForm):
    class Meta:
        model=Farmimage
        fields=['user','image','caption']