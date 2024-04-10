from django.db import models

# Create your models here.
Color = (
    ('Blanco', 'Blanco'),
    ('Negro', 'Negro'),
    ('Rojo', 'Rojo'),
    ('Verde', 'Verde'),
    ('Azul', 'Azul'),
    ('Amarillo', 'Amarillo'),
    ('Gris', 'Gris'),
    ('Naranja', 'Naranja'),
)

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    nombre = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    color = models.CharField(max_length=255, choices = Color)
    idempresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="vehiculo_list")
    
    def __str__(self):
        return self.nombre
