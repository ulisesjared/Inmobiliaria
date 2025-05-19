from django import forms
from .models import Propiedad
from .models import Contacto

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

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'input'}),
            'telefono': forms.TextInput(attrs={'class': 'input'}),
            'me_interesa': forms.Select(attrs={'class': 'input'}),
            'como_contactar': forms.Select(attrs={'class': 'input'}),
            'comentarios': forms.Textarea(attrs={'class': 'input'}),
        }
