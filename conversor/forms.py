from django import forms
from django.core.exceptions import ValidationError

class FormularioBinario(forms.Form):
    # Formulario que recibe el numero binario
    binario = forms.CharField(
            label='Ingrese un numero binario', 
            max_length=64,
        )

    def clean_binario(self):
        data = self.cleaned_data['binario']

        # Validar que el valor ingresado sea un número binario
        if not all(char in '01' for char in data):
            raise ValidationError('Por favor, ingrese un número binario válido.')

        return data.strip()