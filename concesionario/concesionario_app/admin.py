from django.contrib import admin
from concesionario_app.models import Vehiculo
from concesionario_app.models import Empresa

# Register your models here.
admin.site.register(Vehiculo)
admin.site.register(Empresa)
