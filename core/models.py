import qrcode
from django.core.validators import RegexValidator
from django.db import models
from django.utils.safestring import mark_safe

SOLO_TEXTO_REGEX = RegexValidator(r'^[a-zA-Z]+$', 'Solo se admiten letras')


class Ficha(models.Model):
    SEXO_CHOICES = (
        ('m', 'Macho'),
        ('h', 'Hembra'),
    )
    nombre = models.CharField(max_length=255, validators=[SOLO_TEXTO_REGEX])
    identidad = models.CharField(max_length=255, unique=True, )
    color = models.CharField(max_length=255, validators=[SOLO_TEXTO_REGEX])
    raza = models.CharField(max_length=255, validators=[SOLO_TEXTO_REGEX])
    foto = models.ImageField(upload_to='fotos/')
    sexo = models.CharField(max_length=255, choices=SEXO_CHOICES)
    esterilizado = models.BooleanField(default=False)
    peso = models.FloatField()
    qr = models.CharField(max_length=900, blank=True, null=True)
    date_creation = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de registro')

    def __str__(self):
        return self.nombre

    def mostrar_foto(self):
        return mark_safe('<img src="' + self.foto.url + '"  width="80" height="80" class="circular">')

    mostrar_foto.short_description = 'Vista previa'
    mostrar_foto.allow_tags = True

    def mostrar_qr(self):
        imagen = 'A'
        if self.qr is not None:
            imagen = self.qr
        return mark_safe('<img src="/media/' + imagen + '"  width="300" height="300" >')

    mostrar_qr.short_description = 'Código QR'
    mostrar_qr.allow_tags = True

    def save(self, *args, **kwargs):
        if not self.qr:
            qr = qrcode.make()
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=50,
                border=4,
            )
            esterilizado = 'Si' if self.esterilizado else 'No'

            qr.add_data({
                'nombre': str(self.nombre),
                'identidad': str(self.identidad),
                'color': str(self.color),
                'raza': str(self.raza),
                'sexo': str(self.sexo),
                'esterilizado': str(esterilizado),
                'peso': str(self.peso),
            })
            qr.make(fit=True)
            imagen = qr.make_image(fill_color="black", back_color="white").convert('RGB')
            if Ficha.objects.exists():
                pk = Ficha.objects.last().pk + 1
            else:
                pk = 1
            self.qr = "/qr/" + str(pk) + '.png'
            self.save()
            imagen.save("media/qr/" + str(pk) + ".png")
        super(Ficha, self).save(*args, **kwargs)
