from rest_framework import serializers
from concesionario_app.models import Empresa, Vehiculo

class EmpresaSerializer(serializers.ModelFieldSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class VehiculoSerializer(serializers.ModelFieldSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'