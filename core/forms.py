from datetime import datetime

from django import forms
from django.forms import ModelForm

from core.models import Ficha, Visita


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

# class InformeIncidenciaForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     class Meta:
#         model = InformeIncidencia
#         fields = '__all__'
#         exclude = ['date_creation', 'user', 'balita']
#         widgets = {
#             'motive': forms.Textarea(
#                 attrs={
#                     'placeholder': 'Escribe una descripción del problema',
#                     'rows': 5,
#                     'cols': 3,
#                     'class': 'circular'
#                 }
#             )
#         }
#
#
# class InformeReservaForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     class Meta:
#         model = InformeReserva
#         fields = '__all__'
#         exclude = ['date_creation', 'user', 'balita']
#
#     # date_to_reserve = forms.DateField(
#     #     widget=forms.DateInput(
#     #         format='%d/%m/%Y',
#     #         attrs={
#     #             'type': 'date',
#     #         }
#     #     ),
#     #     input_formats=('%d/%m/%Y',)
#     # )
#         widgets = {
#             'date_to_reserve': forms.DateInput(
#                 format='%d/%m/%Y',
#                 attrs={
#                     'class': 'circular',
#                     'type': 'date',
#                 },
#             )
#         }
#
#
# class InformeVentaForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     class Meta:
#         model = InformeVenta
#         fields = '__all__'
#         exclude = ['date_creation', 'user', 'balita']
