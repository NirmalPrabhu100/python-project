from django import forms
from app.models import tableone

class pyclass (forms.ModelForm):
    class Meta:
        model=tableone
        fields=['firstname','lastname']