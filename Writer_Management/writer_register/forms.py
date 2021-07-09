from django import forms
from .models import Writers


class WritersForm(forms.ModelForm):
    
    class Meta:
        model = Writers
        fields = ('__all__')