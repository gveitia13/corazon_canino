from django.contrib import admin

# Register your models here.
from core.models import FotoDenuncia, Denuncia

admin.site.register(FotoDenuncia)
admin.site.register(Denuncia)
