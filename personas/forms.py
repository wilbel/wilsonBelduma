from django import forms
from .models import Persona

class formularioPersona(forms.ModelForm):
 
    class Meta:
        model = Persona
        fields= '__all__'
        widgets = {'nacimiento':forms.DateInput(attrs={'type':'date'})}