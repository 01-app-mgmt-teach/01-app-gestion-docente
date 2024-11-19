from django import forms
from .models import MiPerfil

class PerfilForm(forms.ModelForm):
    class Meta:
        model = MiPerfil
        fields = ['descripcion', 'numero_telefono']
