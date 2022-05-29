from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from core.forms import FichaForm, VisitaForm, EventoForm, InformacionForm
from core.models import Ficha, Visita, Evento, Informacion


class Startpage(generic.TemplateView):
    template_name = 'startpage.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# CRUD Ficha
class FichaListView(generic.ListView, ):
    model = Ficha
    template_name = 'ficha_list.html'
    queryset = Ficha.objects.all()
    success_url = reverse_lazy('ficha_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('ficha_add')
        context['entity'] = 'Ficha'
        context['title'] = 'Listado de fichas'
        return context

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            print(request.POST)
            action = request.POST['action']
            if action == 'ficha-details':
                data = Ficha.objects.get(pk=request.POST['id']).toJSON()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


class FichaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ficha
    template_name = 'form.html'
    form_class = FichaForm
    success_url = reverse_lazy('ficha_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('ficha_add')
        context['entity'] = 'Ficha'
        context['list_url'] = self.success_url
        context['title'] = 'Crear una Ficha'
        return context


class FichaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ficha
    template_name = 'form.html'
    form_class = FichaForm
    success_url = reverse_lazy('ficha_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('ficha_add')
        context['entity'] = 'Ficha'
        context['list_url'] = self.success_url
        context['title'] = 'Actualizar Ficha'
        return context


class FichaDetailsView(LoginRequiredMixin, generic.DetailView):
    model = Ficha
    template_name = 'form.html'
    form_class = FichaForm
    success_url = reverse_lazy('ficha_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('ficha_add')
        context['entity'] = 'Ficha'
        context['list_url'] = self.success_url
        context['title'] = 'Detalles de Ficha'
        return context


class FichaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ficha
    template_name = 'delete.html'
    success_url = reverse_lazy('ficha_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('ficha_add')
        context['entity'] = 'Ficha'
        context['list_url'] = self.success_url
        context['title'] = 'Eliminar Ficha'
        return context


# CRUD Visitante
# class VisitanteListView(LoginRequiredMixin, generic.ListView, ):
#     model = Visitante
#     template_name = 'visitante_list.html'
#     queryset = Visitante.objects.all()
#     success_url = reverse_lazy('visitante_list')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['create_url'] = reverse_lazy('visitante_add')
#         context['entity'] = 'Visitante'
#         context['title'] = 'Listado de visitantes'
#         return context
#
#
# class VisitanteCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Visitante
#     template_name = 'form.html'
#     fields = "__all__"
#     success_url = reverse_lazy('visitante_list')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['create_url'] = reverse_lazy('visitante_add')
#         context['entity'] = 'Visitante'
#         context['list_url'] = self.success_url
#         context['title'] = 'Crear un Visitante'
#         return context
#
#
# class VisitanteUpdateView(LoginRequiredMixin, generic.UpdateView):
#     model = Visitante
#     template_name = 'form.html'
#     fields = "__all__"
#     success_url = reverse_lazy('visitante_list')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['create_url'] = reverse_lazy('visitante_add')
#         context['entity'] = 'Visitante'
#         context['list_url'] = self.success_url
#         context['title'] = 'Editar Visitante'
#         return context
#
#
# class VisitanteDeleteView(LoginRequiredMixin, generic.DeleteView):
#     model = Visitante
#     template_name = 'delete.html'
#     success_url = reverse_lazy('visitante_list')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['create_url'] = reverse_lazy('visitante_add')
#         context['entity'] = 'Visitante'
#         context['list_url'] = self.success_url
#         context['title'] = 'Eliminar Visitante'
#         return context


# CRUD Visita

class VisitaListView(generic.ListView, ):
    model = Visita
    template_name = 'visita_list.html'
    queryset = Visita.objects.all()
    success_url = reverse_lazy('visita-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('visita-add')
        context['entity'] = 'Visita'
        context['title'] = 'Listado de visita'
        return context


class VisitaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Visita
    template_name = 'form.html'
    form_class = VisitaForm
    success_url = reverse_lazy('visita-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('visita-add')
        context['entity'] = 'Visita'
        context['list_url'] = self.success_url
        context['title'] = 'Registrar una visita'
        return context


class VisitaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Visita
    template_name = 'form.html'
    fields = "__all__"
    success_url = reverse_lazy('visita-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('visita-add')
        context['entity'] = 'Visita'
        context['list_url'] = self.success_url
        context['title'] = 'Editar Visita'
        return context


class VisitaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Visita
    template_name = 'delete.html'
    success_url = reverse_lazy('visita-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('visita-add')
        context['entity'] = 'Visita'
        context['list_url'] = self.success_url
        context['title'] = 'Eliminar Visita'
        return context


# CRUD Evento
class EventoListView(generic.ListView, ):
    model = Evento
    template_name = 'evento_list.html'
    queryset = Evento.objects.all()
    success_url = reverse_lazy('evento-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('evento-add')
        context['entity'] = 'Evento'
        context['title'] = 'Listado de eventos'
        return context


class EventoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Evento
    template_name = 'form.html'
    form_class = EventoForm
    success_url = reverse_lazy('evento-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('evento-add')
        context['entity'] = 'Evento'
        context['list_url'] = self.success_url
        context['title'] = 'Registrar un evento'
        return context


class EventoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Evento
    template_name = 'form.html'
    form_class = EventoForm
    success_url = reverse_lazy('evento-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('evento-add')
        context['entity'] = 'Evento'
        context['list_url'] = self.success_url
        context['title'] = 'Editar evento'
        return context


class EventoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Evento
    template_name = 'delete.html'
    success_url = reverse_lazy('evento-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('evento-add')
        context['entity'] = 'Evento'
        context['list_url'] = self.success_url
        context['title'] = 'Eliminar evento'
        return context


# CRUD Informacion
class InformacionListView(generic.ListView, ):
    model = Informacion
    template_name = 'informacion_list.html'
    queryset = Informacion.objects.all()
    success_url = reverse_lazy('informacion-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('informacion-add')
        context['entity'] = 'Información'
        context['title'] = 'Información del proyecto'
        return context


class InformacionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Informacion
    template_name = 'form.html'
    form_class = InformacionForm
    success_url = reverse_lazy('informacion-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('informacion-add')
        context['entity'] = 'Información'
        context['list_url'] = self.success_url
        context['title'] = 'Crear información'
        return context


class InformacionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Informacion
    template_name = 'form.html'
    form_class = InformacionForm
    success_url = reverse_lazy('informacion-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('informacion-add')
        context['entity'] = 'Información'
        context['list_url'] = self.success_url
        context['title'] = 'Editar información'
        return context


class InformacionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Informacion
    template_name = 'delete.html'
    success_url = reverse_lazy('informacion-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('informacion-add')
        context['entity'] = 'Información'
        context['list_url'] = self.success_url
        context['title'] = 'Eliminar Información'
        return context
