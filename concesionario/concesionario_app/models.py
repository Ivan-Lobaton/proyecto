from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    nombre = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre
    
class Propietario(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre
