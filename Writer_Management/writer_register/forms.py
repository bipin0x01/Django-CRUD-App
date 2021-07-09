from django import forms
from .models import Writers, experience


class WritersForm(forms.ModelForm):
    
    class Meta:
        model = Writers
        fields = ('fullname','mobile','experience')
        labels = {
            'fullname':'Full Name',
            'mobile':'Contact No.',
            'experience':'Experience'
        }

    def __init__(self,*args, **kwargs):
        super(WritersForm,self).__init__(*args, **kwargs)
        self.fields['experience'].empty_label = " Select "