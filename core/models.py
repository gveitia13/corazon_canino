from datetime import datetime

import qrcode
from crum import get_current_request
from django.core.validators import RegexValidator, MinLengthValidator, MinValueValidator
from django.db import models
from django.forms import model_to_dict
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

SOLO_TEXTO_REGEX = RegexValidator(r'^[a-zA-Z]+$', 'Solo se admiten letras')
TELEFONO_REGEX = RegexValidator(r'^[\+]?[\d]{5,15}$', 'Formato incorrecto')


class Ficha(models.Model):
    SEXO_CHOICES = (
        ('m', 'Macho'),
        ('h', 'Hembra'),
    )
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    color = models.CharField(max_length=255, verbose_name="Color")
    raza = models.CharField(max_length=255, verbose_name="Raza")
    foto = models.ImageField(upload_to='fotos/', verbose_name="Foto")
    sexo = models.CharField(
        max_length=255, choices=SEXO_CHOICES, verbose_name="Sexo")
    esterilizado = models.BooleanField(
        default=False, verbose_name="Esterilizado")
    peso = models.FloatField(verbose_name="Peso en KG", validators=[
        MinValueValidator(0, 'Debe ser positivo')])
    enfermedades = models.CharField(
        max_length=255, verbose_name='Enfermedades o lesiones', null=True, blank=True)
    qr = models.CharField(max_length=900, blank=True,
                          null=True, verbose_name="Código Qr")
    date_creation = models.DateField(
        auto_now_add=True, null=True, blank=True, verbose_name='Fecha de registro')

    def __str__(self):
        return self.nombre

    def toJSON(self):
        json = model_to_dict(self)
        json['foto'] = self.foto.url
        json['sexo'] = 'Macho' if self.sexo == 'm' else 'Hembra'
        json['esterilizado'] = 'Si' if self.esterilizado else 'No'
        json['enfermedades'] = 'Ninguna' if not self.enfermedades else self.enfermedades
        json['vacunas'] = [i.toJSON() for i in Vacuna.objects.filter(ficha_id=self.pk)] if Vacuna.objects.filter(
            ficha_id=self.pk).exists() else []
        json['desparasitaciones'] = [i.toJSON() for i in Desparasitacion.objects.filter(
            ficha_id=self.pk)] if Desparasitacion.objects.filter(
            ficha_id=self.pk).exists() else []
        return json

    def mostrar_foto(self):
        return mark_safe('<img src="' + self.foto.url + '"  width="80" height="80" class="circular agrandar '
                                                        'cursor-zoom-in">')

    def link_foto(self):
        return mark_safe(f'<a href="{self.foto.url}"> {self.mostrar_foto()}</a>')

    mostrar_foto.short_description = 'Vista previa'
    mostrar_foto.allow_tags = True

    def mostrar_qr(self):
        imagen = 'A'
        if self.qr is not None:
            imagen = self.qr
        return mark_safe('<img src="' + imagen + '"  width="80" height="80" class="agrandar cursor-zoom-in">')

    def link_qr(self):
        return mark_safe(f'<a href="{self.qr}"> {self.mostrar_qr()}</a>')

    mostrar_qr.short_description = 'Código QR'
    mostrar_qr.allow_tags = True

    def save(self, *args, **kwargs):
        request = get_current_request()
        print(request.get_host())
        if not self.qr:
            qr = qrcode.make()
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=20,
                border=4,
            )
            esterilizado = 'Si' if self.esterilizado else 'No'
            qr.add_data({
                'nombre': str(self.nombre),
                'color': str(self.color),
                'raza': str(self.raza),
                'sexo': str(self.sexo),
                'esterilizado': str(esterilizado),
                'peso': str(self.peso),
                'link': f"http://{request.get_host()}/ficha/update/{self.pk}/",
            })
            qr.make(fit=True)
            imagen = qr.make_image(
                fill_color="black", back_color="white").convert('RGB')
            if Ficha.objects.exists():
                pk = Ficha.objects.last().pk + 1
            else:
                pk = 1
            self.qr = "/media/qr/" + str(pk) + '.png'
            self.save()
            imagen.save("media/qr/" + str(pk) + ".png")
        super(Ficha, self).save(*args, **kwargs)


class Visita(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    apellido = models.CharField(max_length=255, verbose_name="Apellidos")
    edad = models.IntegerField(
        null=True, blank=True, verbose_name="Edad (opcional)")
    telefono = models.CharField(max_length=255, null=True, blank=True, verbose_name="Teléfono",
                                validators=[TELEFONO_REGEX])
    ci = models.CharField(max_length=11, validators=[
        MinLengthValidator(11)], verbose_name='Carnet')
    organizacion = models.CharField(
        max_length=255, verbose_name="Organización", null=True, blank=True)
    veterinario = models.BooleanField(
        default=True, verbose_name="Es veterinario")
    fecha = models.DateField(default=datetime.now, verbose_name="Fecha")

    def __str__(self):
        return self.nombre + ' - ' + str(self.fecha)


class Evento(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    foto = models.ImageField(upload_to='fotos/', verbose_name="Foto")
    tipo = models.CharField(max_length=255, verbose_name="Tipo")
    fecha = models.DateTimeField(default=datetime.now, verbose_name="Fecha")
    detalles = models.CharField(max_length=500, verbose_name="Detalles")

    def __str__(self):
        return self.nombre

    def mostrar_foto(self):
        return mark_safe('<img src="' + self.foto.url + '"  width="80" height="80" class="circular agrandar '
                                                        'cursor-zoom-in">')

    mostrar_foto.short_description = 'Vista previa'
    mostrar_foto.allow_tags = True


class Informacion(models.Model):
    foto = models.ImageField(upload_to='fotos/', verbose_name="Foto")
    title = models.CharField(
        max_length=50, verbose_name="Titulo", null=True, blank=True)
    texto = models.CharField(max_length=900, verbose_name="Texto")

    def __str__(self):
        return self.title


class Contacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellidos")
    area = models.CharField(max_length=100, verbose_name="Facultad o área", choices=(
        ('f1', 'Facultad 1'),
        ('f2', 'Facultad 3'),
        ('f3', 'Facultad 3'),
        ('f4', 'Facultad 4'),
        ('fte', 'Facultad FTE'),
        ('citec', 'Facultad CITEC'),
        ('otro', 'Otro'),
    ))
    cargo = models.CharField(
        max_length=150, verbose_name='Cargo', null=True, blank=True)
    telefono = models.CharField(verbose_name='Teléfono', max_length=20,
                                help_text='Puede empezar con +, el resto solo dígitos',
                                validators=[TELEFONO_REGEX])

    def __str__(self):
        return self.nombre


class Asociado(models.Model):
    foto = models.ImageField(upload_to='fotos/', verbose_name="Foto")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    telefono = models.CharField(verbose_name='Teléfono', max_length=20,
                                validators=[TELEFONO_REGEX])
    link = models.URLField(max_length=900, verbose_name='Link de contacto')

    def __str__(self):
        return self.nombre

    def mostrar_foto(self):
        return mark_safe('<img src="' + self.foto.url + '"  width="80" height="80" class="circular agrandar '
                                                        'cursor-zoom-in">')

    def link_foto(self):
        return mark_safe(f'<a href="{self.foto.url}"> {self.mostrar_foto()}</a>')


class Enfermedad(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.CharField(max_length=900, verbose_name='Descripción')

    def __str__(self):
        return self.nombre


class Denuncia(models.Model):
    descripcion = models.CharField(verbose_name='Descripción', max_length=500)
    ubicacion = models.CharField(
        verbose_name='Ubicación (opcional)', max_length=255, null=True, blank=True)
    caracteristicas = models.CharField(
        verbose_name='Características del animal', max_length=255, )
    foto = models.ImageField(
        upload_to='fotos/', verbose_name="Evidencia (foto)", )
    date_creation = models.DateField(
        auto_now_add=True, null=True, blank=True, verbose_name='Fecha de registro')

    def __str__(self):
        return self.descripcion

    class Meta:
        ordering = ['date_creation']

    def mostrar_foto(self):
        return mark_safe('<img src="' + self.foto.url + '"  width="80" height="80" class="circular agrandar '
                                                        'cursor-zoom-in">')

    def link_foto(self):
        return mark_safe(f'<a href="{self.foto.url}"> {self.mostrar_foto()}</a>')


class Vacuna(models.Model):
    ficha = models.ForeignKey(
        Ficha, on_delete=models.CASCADE, verbose_name='Ficha a vacunar', )
    fecha = models.DateField(
        verbose_name='Fecha de vacunación', default=datetime.utcnow)
    producto = models.CharField(verbose_name='Producto', max_length=100)
    fecha_siguiente = models.DateField(
        verbose_name='Fecha de la próxima vacuna')

    def __str__(self):
        return self.producto

    class Meta:
        ordering = ['-fecha']

    def toJSON(self):
        json = model_to_dict(self)
        json['ficha'] = str(self.ficha)
        json['fecha'] = self.fecha
        json['fecha_siguiente'] = self.fecha_siguiente
        return json


class Desparasitacion(models.Model):
    ficha = models.ForeignKey(
        Ficha, on_delete=models.CASCADE, verbose_name='Ficha a desparasitar', )
    fecha = models.DateField(
        verbose_name='Fecha de vacunación', default=datetime.utcnow)
    tipo = models.CharField(max_length=100, choices=(
        ('externa', 'Desparasitación externa'),
        ('interna', 'Desparasitación interna'),), verbose_name='Tipo')
    peso = models.FloatField(verbose_name='Peso', validators=[
        MinValueValidator(0, 'Debe ser positivo')])

    def __str__(self):
        return self.tipo

    def toJSON(self):
        json = model_to_dict(self)
        json['tipo'] = self.get_tipo_display()
        json['ficha'] = str(self.ficha)
        json['fecha'] = self.fecha
        return json

    class Meta:
        ordering = ('-fecha',)


class Medicamento(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    descripcion = models.CharField(max_length=500, verbose_name='Descripcion')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')

    def __str__(self):
        return self.nombre
