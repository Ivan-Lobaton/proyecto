# Generated by Django 5.0.4 on 2024-04-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('correo', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('modelo', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('fabricante', models.CharField(max_length=255)),
                ('pais', models.CharField(max_length=255)),
            ],
        ),
    ]
