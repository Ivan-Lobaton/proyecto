from rest_framework.response import Response
from concesionario_app.admin import Empresa, Vehiculo
from concesionario_app.api.serializers import EmpresaSerializer, VehiculoSerializer

from rest_framework.views import APIView
from rest_framework import status

class EmpresaAV(APIView):
    def get(self, request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmpresaDetalleAV(APIView):
    def get(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmpresaSerializer(empresa, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'},status=status.HTTP_404_NOT_FOUND)
        serializer = EmpresaSerializer(empresa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'},status=status.HTTP_404_NOT_FOUND)
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VehiculoAV(APIView):
    def get(self, request):
        vehiculos = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculos, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = VehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VehiculoDetalleAV(APIView):
    def get(self, request, pk):
        try:
            vehiculo = Vehiculo.objects.get(pk=pk)
        except Vehiculo.DoesNotExist:
            return Response({'error': 'Vehiculo no encontrado'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = VehiculoSerializer(vehiculo, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            vehiculo = Vehiculo.objects.get(pk=pk)
        except Vehiculo.DoesNotExist:
            return Response({'error': 'Vehiculo no encontrado'},status=status.HTTP_404_NOT_FOUND)
        serializer = VehiculoSerializer(vehiculo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def deleate(self, request, pk):
        try:
            vehiculo = Vehiculo.objects.get(pk=pk)
        except Vehiculo.DoesNotExist:
            return Response({'error': 'Vehiculo no encontrado'},status=status.HTTP_404_NOT_FOUND)
        vehiculo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    