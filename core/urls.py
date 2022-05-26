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
]
