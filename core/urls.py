from django.urls import path

from core.views import *

urlpatterns = [
    # Ficha
    path('ficha/list/', FichaListView.as_view(), name='ficha_list'),
    path('ficha/add/', FichaCreateView.as_view(), name='ficha_add'),
    path('ficha/update/<int:pk>/', FichaUpdateView.as_view(), name='ficha_update'),
    path('ficha/details/<int:pk>/', FichaDetailsView.as_view(), name='ficha_details'),
    path('ficha/delete/<int:pk>/', FichaDeleteView.as_view(), name='ficha_delete'),
    # Visitante
    path('visitante/list/', VisitanteListView.as_view(), name='visitante_list'),
    path('visitante/add/', VisitanteCreateView.as_view(), name='visitante_add'),
    path('visitante/update/<int:pk>/', VisitanteUpdateView.as_view(), name='visitante_update'),
    path('visitante/delete/<int:pk>/', VisitanteDeleteView.as_view(), name='visitante_delete'),
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
]
