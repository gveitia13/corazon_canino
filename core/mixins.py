from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class ClientPermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

    def get_perms(self):
        perms = []
        if isinstance(self.permission_required, str):
            perms.append(self.permission_required)
        else:
            perms = list(self.permission_required)
        return perms

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('index')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        request = request
        print(request.user.role)
        if request.user.role == 'client' or request.user.role == 'admin':
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tienes permiso para ingresar a este modulo')
        return HttpResponseRedirect(self.get_url_redirect())


class AdminPermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

    def get_perms(self):
        perms = []
        if isinstance(self.permission_required, str):
            perms.append(self.permission_required)
        else:
            perms = list(self.permission_required)
        return perms

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('index')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        request = request
        print(request.user.role)
        if request.user.role == 'admin':
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tienes permiso para ingresar a este modulo')
        return HttpResponseRedirect(self.get_url_redirect())
