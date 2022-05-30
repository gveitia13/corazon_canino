from datetime import datetime

from django import forms
from django.forms import ModelForm

from core.models import Ficha, Visita, Evento, Informacion, Enfermedad


class FichaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Ficha
        fields = '__all__'
        exclude = ['date_creation', 'qr', ]


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
