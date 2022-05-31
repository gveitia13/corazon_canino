from django.urls import path

from core.views import *

urlpatterns = [
    # Ficha
    path('ficha/list/', FichaListView.as_view(), name='ficha_list'),
    path('ficha/add/', FichaCreateView.as_view(), name='ficha_add'),
    path('ficha/update/<int:pk>/', FichaUpdateView.as_view(), name='ficha_update'),
    path('ficha/details/<int:pk>/', FichaDetailsView.as_view(), name='ficha_details'),
    path('ficha/delete/<int:pk>/', FichaDeleteView.as_view(), name='ficha_delete'),
    # Visita
    path('visitas/list/', VisitaListView.as_view(), name='visita-list'),
    path('visitas/add/', VisitaCreateView.as_view(), name='visita-add'),
    path('visitas/update/<int:pk>/', VisitaUpdateView.as_view(), name='visita-update'),
    path('visitas/delete/<int:pk>/', VisitaDeleteView.as_view(), name='visita-delete'),
    # Evento
    path('evento/list/', EventoListView.as_view(), name='evento-list'),
    path('evento/add/', EventoCreateView.as_view(), name='evento-add'),
    path('evento/update/<int:pk>/', EventoUpdateView.as_view(), name='evento-update'),
    path('evento/delete/<int:pk>/', EventoDeleteView.as_view(), name='evento-delete'),
    # Informacion
    path('informacion/list/', InformacionListView.as_view(), name='informacion-list'),
    path('informacion/add/', InformacionCreateView.as_view(), name='informacion-add'),
    path('informacion/update/<int:pk>/', InformacionUpdateView.as_view(), name='informacion-update'),
    path('informacion/delete/<int:pk>/', InformacionDeleteView.as_view(), name='informacion-delete'),
    # Contacto
    path('contacto/list/', ContactoListView.as_view(), name='contacto-list'),
    path('contacto/add/', ContactoCreateView.as_view(), name='contacto-add'),
    path('contacto/update/<int:pk>/', ContactoUpdateView.as_view(), name='contacto-update'),
    path('contacto/delete/<int:pk>/', ContactoDeleteView.as_view(), name='contacto-delete'),
    # Asociado
    path('asociado/list/', AsociadoListView.as_view(), name='asociado-list'),
    path('asociado/add/', AsociadoCreateView.as_view(), name='asociado-add'),
    path('asociado/update/<int:pk>/', AsociadoUpdateView.as_view(), name='asociado-update'),
    path('asociado/delete/<int:pk>/', AsociadoDeleteView.as_view(), name='asociado-delete'),
    # Enfermedad
    path('enfermedad/list/', EnfermedadListView.as_view(), name='enfermedad-list'),
    path('enfermedad/add/', EnfermedadCreateView.as_view(), name='enfermedad-add'),
    path('enfermedad/update/<int:pk>/', EnfermedadUpdateView.as_view(), name='enfermedad-update'),
    path('enfermedad/delete/<int:pk>/', EnfermedadDeleteView.as_view(), name='enfermedad-delete'),
    # Denuncia
    path('denuncia/list/', DenunciaListView.as_view(), name='denuncia-list'),
    path('denuncia/add/', DenunciaCreateView.as_view(), name='denuncia-add'),
    path('denuncia/update/<int:pk>/', DenunciaUpdateView.as_view(), name='denuncia-update'),
    path('denuncia/delete/<int:pk>/', DenunciaDeleteView.as_view(), name='denuncia-delete'),
    # Vacuna
    path('vacuna/list/', VacunaListView.as_view(), name='vacuna-list'),
    path('vacuna/add/',VacunaCreateView.as_view(), name='vacuna-add'),
    path('vacuna/update/<int:pk>/', VacunaUpdateView.as_view(), name='vacuna-update'),
    path('vacuna/delete/<int:pk>/', VacunaDeleteView.as_view(), name='vacuna-delete'),
    # Desparasitacion
    path('desparasitacion/list/', DesparasitacionListView.as_view(), name='desparasitacion-list'),
    path('desparasitacion/add/',DesparasitacionCreateView.as_view(), name='desparasitacion-add'),
    path('desparasitacion/update/<int:pk>/', DesparasitacionUpdateView.as_view(), name='desparasitacion-update'),
    path('desparasitacion/delete/<int:pk>/', DesparasitacionDeleteView.as_view(), name='desparasitacion-delete'),
    # Medicamento
    path('medicamento/list/', MedicamentoListView.as_view(), name='medicamento-list'),
    path('medicamento/add/', MedicamentoCreateView.as_view(), name='medicamento-add'),
    path('medicamento/update/<int:pk>/', MedicamentoUpdateView.as_view(), name='medicamento-update'),
    path('medicamento/delete/<int:pk>/', MedicamentoDeleteView.as_view(), name='medicamento-delete'),
]
