from datetime import datetime

from django import forms
from django.forms import ModelForm

from core.models import Ficha, Visita, Evento, Informacion, Enfermedad, Denuncia, Vacuna, Desparasitacion, Medicamento


class FichaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Ficha
        fields = '__all__'
        exclude = ['date_creation', 'qr', ]
        widgets = {
            'enfermedades': forms.Textarea(
                attrs={
                    'placeholder': 'Enfermedades que padece',
                    'rows': 5,
                    'cols': 3,
                    'class': 'circular'
                }
            ),
        }


class VisitaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Visita
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'class': 'circular',
                    'type': 'date',
                }
            )
        }


class EventoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Evento
        fields = '__all__'
        widgets = {
            'detalles': forms.Textarea(
                attrs={
                    'placeholder': 'Detalles del evento',
                    'rows': 5,
                    'cols': 3,
                    'class': 'circular'
                }
            ),
            'fecha': forms.DateTimeInput(
                attrs={
                    'class': 'circular',
                    'type': 'datetime-local',
                }
            )
        }


class InformacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Informacion
        fields = '__all__'
        widgets = {
            'texto': forms.Textarea(
                attrs={
                    'placeholder': 'Escriba el texto',
                    'rows': 7,
                    'cols': 3,
                    'class': 'circular'
                }
            ),
        }


class EnfermedadForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Enfermedad
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(
                attrs={
                    'placeholder': 'Escriba la descripción',
                    'rows': 7,
                    'cols': 3,
                    'class': 'circular'
                }
            ),
        }


class DenunciaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Denuncia
        fields = '__all__'
        exclude = ('date_creation',)
        widgets = {
            'descripcion': forms.Textarea(
                attrs={
                    'placeholder': 'Especifique los motivos de su denuncia',
                    'rows': 3,
                    'cols': 3,
                    'class': 'circular'
                }
            ),
            'caracteristicas': forms.Textarea(
                attrs={
                    'placeholder': 'Describa al animal',
                    'rows': 2,
                    'cols': 3,
                    'class': 'circular'
                }
            ),
            'ubicacion': forms.TextInput(
                attrs={
                    'placeholder': 'Ubicación de los hechos'
                }
            )
        }


class VacunaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Vacuna
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(
                attrs={
                    'class': 'circular',
                    'type': 'date',
                }
            ),
            'fecha_siguiente': forms.DateInput(
                attrs={
                    'class': 'circular',
                    'type': 'date',
                }
            ),
        }


class DesparasitacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Desparasitacion
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(
                attrs={
                    'class': 'circular',
                    'type': 'date',
                }
            ),
        }


class MedicamentoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Medicamento
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(
                attrs={
                    'placeholder': '',
                    'rows': 3,
                    'cols': 3,
                    'class': 'circular'
                }
            ),
        }
