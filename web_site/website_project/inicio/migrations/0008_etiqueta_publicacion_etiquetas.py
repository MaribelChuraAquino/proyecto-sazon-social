# Generated by Django 5.1.1 on 2024-09-18 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0007_grupo_foto_perfil_grupo_portada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='publicacion',
            name='etiquetas',
            field=models.ManyToManyField(blank=True, to='inicio.etiqueta'),
        ),
    ]
