
from django import forms

class QRCodeGenerationForm(forms.Form):
    foreground_color = forms.CharField(max_length=7, required=True, label='Foreground Color', widget=forms.TextInput(attrs={'type': 'color'}))
    background_color = forms.CharField(max_length=7, required=True, label='Background Color', widget=forms.TextInput(attrs={'type': 'color'}))
