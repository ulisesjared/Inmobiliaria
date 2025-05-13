from django import forms
from .models import Propiedad

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = [
            'foto_principal',
            'titulo',
            'descripcion',
            'ubicacion',
            'precio',
            'tipo_compra',
            'tipo_inmueble',
            'numero_recamaras',
        ]

