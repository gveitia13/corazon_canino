import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.http import JsonResponse, HttpRequest
from django.shortcuts import render, redirect
from django.template.loader import get_template, render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from core.forms import FichaForm, VisitaForm, EventoForm, InformacionForm, EnfermedadForm, DenunciaForm, VacunaForm, \
    DesparasitacionForm, MedicamentoForm
from core.models import Ficha, Visita, Evento, Informacion, Contacto, Asociado, Enfermedad, Denuncia, Vacuna, \
    Desparasitacion, Medicamento, FotoDenuncia
from proyecto_canino import settings


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

    def get_queryset(self):
        qs = super(FichaListView, self).get_queryset()
        if self.request.GET.get('search'):
            qs = qs.filter(nombre__icontains=self.request.GET.get('search'))
        return qs


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


class FichaDetailsView(generic.DetailView):
    template_name = 'ficha_details.html'
    model = Ficha

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = 'Ficha'
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

    def get_queryset(self):
        qs = super(VisitaListView, self).get_queryset()
        if self.request.GET:
            if not self.request.GET.get('initial') or not self.request.GET.get('end'):
                return qs
            qs = qs.filter(fecha__range=[self.request.GET.get('initial'), self.request.GET.get('end')])
        return qs


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
        # self.request.get_host()
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

    def get_queryset(self):
        qs = super(EventoListView, self).get_queryset()
        if self.request.GET:
            if not self.request.GET.get('initial') or not self.request.GET.get('end'):
                return qs
            qs = qs.filter(fecha__range=[self.request.GET.get('initial'), self.request.GET.get('end')])
        return qs


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


# CRUD Contacto
class ContactoListView(generic.ListView, ):
    model = Contacto
    template_name = 'contacto_list.html'
    queryset = Contacto.objects.all()
    success_url = reverse_lazy('contacto-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('contacto-add')
        context['entity'] = 'Contacto'
        context['title'] = 'Listado de miembros del proyecto'
        return context


class ContactoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Contacto
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('contacto-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('contacto-add')
        context['entity'] = 'Contacto'
        context['list_url'] = self.success_url
        context['title'] = 'Crear Contacto'
        return context


class ContactoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Contacto
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('contacto-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('contacto-add')
        context['entity'] = 'Contacto'
        context['list_url'] = self.success_url
        context['title'] = 'Editar Contacto'
        return context


class ContactoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Contacto
    template_name = 'delete.html'
    success_url = reverse_lazy('contacto-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('contacto-add')
        context['entity'] = 'Contacto'
        context['list_url'] = self.success_url
        context['title'] = 'Eliminar Contacto'
        return context


# CRUD Asociado
class AsociadoListView(generic.ListView, ):
    model = Asociado
    template_name = 'asociado_list.html'
    queryset = Asociado.objects.all()
    success_url = reverse_lazy('asociado-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('asociado-add')
        context['entity'] = 'Asociado'
        context['title'] = 'Listado de asociados al proyecto'
        return context


class AsociadoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Asociado
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('asociado-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('asociado-add')
        context['entity'] = 'Asociado'
        context['list_url'] = self.success_url
        context['title'] = 'Crear Asociado'
        return context


class AsociadoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Asociado
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('asociado-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('asociado-add')
        context['entity'] = 'Asociado'
        context['list_url'] = self.success_url
        context['title'] = 'Editar Asociado'
        return context


class AsociadoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Asociado
    template_name = 'delete.html'
    success_url = reverse_lazy('asociado-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('asociado-add')
        context['entity'] = 'Asociado'
        context['list_url'] = self.success_url
        context['title'] = 'Eliminar Asociado'
        return context


# CRUD Enfermedad
class EnfermedadListView(generic.ListView, ):
    model = Enfermedad
    template_name = 'enfermedad_list.html'
    queryset = Enfermedad.objects.all()
    success_url = reverse_lazy('enfermedad-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('enfermedad-add')
        context['entity'] = 'Enfermedad'
        context['title'] = 'Enfermedades más comunes'
        return context


class EnfermedadCreateView(LoginRequiredMixin, generic.CreateView):
    model = Enfermedad
    template_name = 'form.html'
    form_class = EnfermedadForm
    success_url = reverse_lazy('enfermedad-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('enfermedad-add')
        context['entity'] = 'Enfermedad'
        context['list_url'] = self.success_url
        context['title'] = 'Registrar Enfermedad'
        return context


class EnfermedadUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Enfermedad
    template_name = 'form.html'
    form_class = EnfermedadForm
    success_url = reverse_lazy('enfermedad-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('enfermedad-add')
        context['entity'] = 'Enfermedad'
        context['list_url'] = self.success_url
        context['title'] = 'Editar Enfermedad'
        return context


class EnfermedadDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Enfermedad
    template_name = 'delete.html'
    success_url = reverse_lazy('enfermedad-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('enfermedad-add')
        context['entity'] = 'Enfermedad'
        context['list_url'] = self.success_url
        context['title'] = 'Eliminar Enfermedad'
        return context


# CRUD Denuncia
class DenunciaListView(LoginRequiredMixin, generic.ListView, ):
    model = Denuncia
    template_name = 'denuncia_list.html'
    queryset = Denuncia.objects.all()
    success_url = reverse_lazy('denuncia-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('denuncia-add')
        context['entity'] = 'Denuncia'
        context['title'] = 'Listados de denuncias'
        return context

    def get_queryset(self):
        qs = super(DenunciaListView, self).get_queryset()
        if self.request.GET:
            if not self.request.GET.get('initial') or not self.request.GET.get('end'):
                return qs
            qs = qs.filter(date_creation__range=[self.request.GET.get('initial'), self.request.GET.get('end')])
        return qs


class DenunciaCreateView(generic.TemplateView):
    model = Denuncia
    template_name = 'denuncia_form.html'
    form_class = DenunciaForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('denuncia-add')
        context['entity'] = 'Denuncia'
        context['list_url'] = self.success_url
        context['title'] = 'Crear Denuncia'
        context['form'] = self.form_class
        return context

    def post(self, request: HttpRequest, *args: list, **kwargs: dict):
        denuncia = Denuncia()
        denuncia.caracteristicas = request.POST.get('caracteristicas', None)
        denuncia.descripcion = request.POST.get('descripcion', None)
        denuncia.ubicacion = request.POST.get('ubicacion', None)
        tipo = ''
        coma = ','
        if request.POST.get('tipo') is not None:
            for t, c in zip(request.POST.getlist('tipo'), range(len(request.POST.getlist('tipo')))):
                if c == len(request.POST.getlist('tipo')) - 1:
                    coma = ''
                tipo += f'{t}{coma} '
        denuncia.tipo = tipo
        denuncia.save()
        if request.FILES:
            for f in request.FILES.getlist('image'):
                foto = FotoDenuncia()
                foto.foto = f
                foto.denuncia_id = denuncia.pk
                foto.save()
        try:
            mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            mailServer.starttls()
            mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

            mensaje = MIMEMultipart()
            mensaje['From'] = settings.EMAIL_HOST_USER
            mensaje['To'] = 'gveitia13@gmail.com'
            mensaje['Subject'] = 'Nueva denuncia'
            content = render_to_string('email.html', {'object': denuncia})
            mensaje.attach(MIMEText(content, 'html'))

            for i in denuncia.fotodenuncia_set.all():
                file = open(os.path.join(os.getcwd(), 'media/', i.foto.name), 'rb')
                contenido = MIMEImage(file.read())
                contenido.add_header('Content-Disposition', f'attachment; filename = "{i.foto.name}"')
                mensaje.attach(contenido)

            mailServer.sendmail(settings.EMAIL_HOST_USER,
                                'gveitia13@gmail.com',
                                mensaje.as_string())

        except Exception as a:
            print(a)
            return JsonResponse({}, safe=False)
        return redirect(reverse_lazy('index'))


class DenunciaUpdateView(generic.UpdateView):
    model = Denuncia
    template_name = 'form.html'
    form_class = DenunciaForm
    success_url = reverse_lazy('denuncia-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('denuncia-add')
        context['entity'] = 'Denuncia'
        context['list_url'] = self.success_url
        context['title'] = 'Editar Denuncia'
        return context


class DenunciaDeleteView(generic.DeleteView):
    model = Denuncia
    template_name = 'delete.html'
    success_url = reverse_lazy('denuncia-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('denuncia-add')
        context['entity'] = 'Denuncia'
        context['list_url'] = self.success_url
        context['title'] = 'Eliminar Denuncia'
        return context


# CRUD Vacuna
class VacunaListView(LoginRequiredMixin, generic.ListView, ):
    model = Vacuna
    template_name = 'vacuna_list.html'
    queryset = Vacuna.objects.all()
    success_url = reverse_lazy('vacuna-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('vacuna-add')
        context['entity'] = 'Vacuna'
        context['title'] = 'Listados de vacunas'
        return context

    def get_queryset(self):
        qs = super(VacunaListView, self).get_queryset()
        if self.request.GET:
            if not self.request.GET.get('initial') or not self.request.GET.get('end'):
                return qs
            qs = qs.filter(fecha__range=[self.request.GET.get('initial'), self.request.GET.get('end')])
        return qs


class VacunaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Vacuna
    template_name = 'form.html'
    form_class = VacunaForm
    success_url = reverse_lazy('vacuna-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('vacuna-add')
        context['entity'] = 'Vacuna'
        context['list_url'] = self.success_url
        context['title'] = 'Crear Vacuna'
        return context


class VacunaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Vacuna
    template_name = 'form.html'
    form_class = VacunaForm
    success_url = reverse_lazy('vacuna-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('vacuna-add')
        context['entity'] = 'Vacuna'
        context['list_url'] = self.success_url
        context['title'] = 'Editar Vacuna'
        return context


class VacunaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Vacuna
    template_name = 'delete.html'
    success_url = reverse_lazy('vacuna-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('vacuna-add')
        context['entity'] = 'Vacuna'
        context['list_url'] = self.success_url
        context['title'] = 'Eliminar Vacuna'
        return context


# CRUD Desparacitacion
class DesparasitacionListView(LoginRequiredMixin, generic.ListView, ):
    model = Desparasitacion
    template_name = 'desparasitacion_list.html'
    queryset = Desparasitacion.objects.all()
    success_url = reverse_lazy('desparasitacion-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('desparasitacion-add')
        context['entity'] = 'Desparasitacion'
        context['title'] = 'Listados de desparasitaciones'
        return context

    def get_queryset(self):
        qs = super(DesparasitacionListView, self).get_queryset()
        if self.request.GET:
            if not self.request.GET.get('initial') or not self.request.GET.get('end'):
                return qs
            qs = qs.filter(fecha__range=[self.request.GET.get('initial'), self.request.GET.get('end')])
        return qs


class DesparasitacionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Desparasitacion
    template_name = 'form.html'
    form_class = DesparasitacionForm
    success_url = reverse_lazy('desparasitacion-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('desparasitacion-add')
        context['entity'] = 'Desparasitacion'
        context['list_url'] = self.success_url
        context['title'] = 'Registrar desparasitacion'
        return context


class DesparasitacionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Desparasitacion
    template_name = 'form.html'
    form_class = DesparasitacionForm
    success_url = reverse_lazy('desparasitacion-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('desparasitacion-add')
        context['entity'] = 'Desparasitacion'
        context['list_url'] = self.success_url
        context['title'] = 'Editar desparasitacion'
        return context


class DesparasitacionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Desparasitacion
    template_name = 'delete.html'
    success_url = reverse_lazy('desparasitacion-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('desparasitacion-add')
        context['entity'] = 'Desparasitacion'
        context['list_url'] = self.success_url
        context['title'] = 'Eliminar desparasitacion'
        return context


# CRUD Medicamento
class MedicamentoListView(generic.ListView, ):
    model = Medicamento
    template_name = 'medicamento_list.html'
    queryset = Medicamento.objects.all()
    success_url = reverse_lazy('medicamento-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('medicamento-add')
        context['entity'] = 'Medicamento'
        context['title'] = 'Medicamentos disponibles'
        return context


class MedicamentoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Medicamento
    template_name = 'form.html'
    form_class = MedicamentoForm
    success_url = reverse_lazy('medicamento-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('medicamento-add')
        context['entity'] = 'Medicamento'
        context['list_url'] = self.success_url
        context['title'] = 'Registrar medicamento'
        return context


class MedicamentoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Medicamento
    template_name = 'form.html'
    form_class = MedicamentoForm
    success_url = reverse_lazy('medicamento-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('medicamento-add')
        context['entity'] = 'Medicamento'
        context['list_url'] = self.success_url
        context['title'] = 'Editar medicamento'
        return context


class MedicamentoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Medicamento
    template_name = 'delete.html'
    success_url = reverse_lazy('medicamento-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('medicamento-add')
        context['entity'] = 'Medicamento'
        context['list_url'] = self.success_url
        context['title'] = 'Eliminar medicamento'
        return context
