# Generated by Django 5.0.6 on 2024-06-27 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de Marca')),
                ('nombreMarca', models.CharField(blank=True, max_length=50, verbose_name='Nombre Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('productoId', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Producto')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='Imagen')),
                ('precio', models.IntegerField(blank=True, null=True, verbose_name='Precio')),
            ],
        ),
    ]
