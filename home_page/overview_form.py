from django import forms
from .models import Overview

class OverviewForm(forms.ModelForm):
    class Meta:
        model=Overview
        fields=['Fid','Assets','Number']