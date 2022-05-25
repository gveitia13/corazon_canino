from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from core.forms import FichaForm
from core.models import Ficha


class Startpage(generic.TemplateView):
    template_name = 'startpage.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# CRUD Ficha
class FichaListView(LoginRequiredMixin, generic.ListView, ):
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
