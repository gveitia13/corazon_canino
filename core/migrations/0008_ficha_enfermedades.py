# Generated by Django 4.0.4 on 2022-05-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_asociado_apellido'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='enfermedades',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Enfermedades'),
        ),
    ]
