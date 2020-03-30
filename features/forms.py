from .models import TaskFeatures
from django import forms


class featureForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title Please'}))
    date_to_complete = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mon/date/year'}))

    class Meta:
        model = TaskFeatures
        exclude = ['user']