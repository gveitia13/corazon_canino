# Generated by Django 4.0.4 on 2022-06-24 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_medicamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='denuncia',
            name='foto',
        ),
        migrations.AlterField(
            model_name='denuncia',
            name='ubicacion',
            field=models.CharField(max_length=255, verbose_name='Ubicación'),
        ),
        migrations.CreateModel(
            name='FotoDenuncia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='fotos/', verbose_name='Evidencia (foto)')),
                ('denuncia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.denuncia')),
            ],
        ),
    ]
