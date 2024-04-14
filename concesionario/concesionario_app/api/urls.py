from django.urls import path
from concesionario_app.api.views import EmpresaAV, EmpresaDetalleAV
from concesionario_app.api.views import VehiculoAV, VehiculoDetalleAV

urlpatterns = [
    path('empresa/', EmpresaAV.as_view(), name='empresa-list'),
    path('empresa/<int:pk>', EmpresaDetalleAV.as_view(), name='empresa-detalles'),
    path('vehiculo/', VehiculoAV.as_view(), name='empresa-list'),
    path('vehiculo/<int:pk>', VehiculoDetalleAV.as_view(), name='empresa-detalles'),
]
