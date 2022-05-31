# Generated by Django 4.0.4 on 2022-05-29 08:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_ficha_identidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('area', models.CharField(choices=[('f1', 'Facultad 1'), ('f2', 'Facultad 3'), ('f3', 'Facultad 3'), ('f4', 'Facultad 4'), ('fte', 'Facultad FTE'), ('citec', 'Facultad CITEC')], max_length=100, verbose_name='Facultad o área')),
                ('cargo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Cargo')),
                ('telefono', models.CharField(help_text='Puede empezar con +, el resto solo dígitos', max_length=20, validators=[django.core.validators.RegexValidator('^[\\+]?[\\d]{5,15}$', 'Formato incorrecto')], verbose_name='Teléfono')),
            ],
        ),
    ]