from django.urls import path

from core.views import *

urlpatterns = [
    # Ficha
    path('ficha/list/', FichaListView.as_view(), name='ficha_list'),
    path('ficha/add/', FichaCreateView.as_view(), name='ficha_add'),
    path('ficha/update/<int:pk>/', FichaUpdateView.as_view(), name='ficha_update'),
    path('ficha/details/<int:pk>/', FichaDetailsView.as_view(), name='ficha_details'),
    path('ficha/delete/<int:pk>/', FichaDeleteView.as_view(), name='ficha_delete'),
    # # Incidencias
    # path('incidencia/list/', IncidenciaListView.as_view(), name='incidencia_list'),
    # path('incidencia/add/', IncidenciaCreateView.as_view(), name='incidencia_add'),
    # path('incidencia/update/<int:pk>/', IncidenciaUpdateView.as_view(), name='incidencia_update'),
    # path('incidencia/delete/<int:pk>/', IncidenciaDeleteView.as_view(), name='incidencia_delete'),
    # # Reservas
    # path('reserva/list/', ReservaListView.as_view(), name='reserva_list'),
    # path('reserva/add/', ReservaCreateView.as_view(), name='reserva_add'),
    # path('reserva/update/<int:pk>/', ReservaUpdateView.as_view(), name='reserva_update'),
    # path('reserva/delete/<int:pk>/', ReservaDeleteView.as_view(), name='reserva_delete'),
    # # Ventas
    # path('venta/list/', VentaListView.as_view(), name='venta_list'),
    # path('venta/add/', VentaCreateView.as_view(), name='venta_add'),
    # path('venta/update/<int:pk>/', VentaUpdateView.as_view(), name='venta_update'),
    # path('venta/delete/<int:pk>/', VentaDeleteView.as_view(), name='venta_delete'),
]
