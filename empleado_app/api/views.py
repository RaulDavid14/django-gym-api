from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status
from empleado_app.models import Empleado 
from .serializers import *

#agregar validacion de la fecha de hoy solamente.

class EmpleadoAV(APIView):
    def get(self, requets):
        try:
            if Empleado.objects.exists():
                empleados = Empleado.objects.all()
                serializer = EmpleadoSerializer(empleados, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else :
                return Response({"message": "No hay no hay registros."}, status = status.HTTP_404_NOT_FOUND)
        except Empleado.DoesNotExist: #excepcion lanzada en caso de no encontrar el campo solicitado
            return Response({"message": "No hay registros."}, status = status.HTTP_404_NOT_FOUND)
    
    
    def post(self, request):
        serializer = EmpleadoSerializer(data=request.data)
        
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            #hacer algo en caso contrario.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpleadoDetailAV(APIView):
    def __search_by_id(self, id):
        try:
            empleado = Empleado.objects.get(id_empleado = id)
            return empleado
        except Empleado.DoesNotExist:
            return None
   
    def get(self, request, valor):
        pempleado = self.__search_by_id(valor)
        if pempleado is None:
            return Response({"message": "No se encontró el usuario"}, status = status.HTTP_404_NOT_FOUND)
        else:    
            serializer = EmpleadoSerializer(pempleado)
            return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, valor):
        pempleado = self.__search_by_id(valor)
        if pempleado is None:
            return Response({"message": "No se encontró el registro"}, status = status.HTTP_404_NOT_FOUND)
        else:
            response = {
                "message" : "Se actualizó el registro",
            }        
            serializer = EmpleadoSerializer(pempleado, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                response["detail"] = serializer.data
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, valor):
        empleado = self.__search_by_id(valor)
        if empleado is None:
           return Response({"message": "No se encontró el usuario"}, status = status.HTTP_404_NOT_FOUND)
        else:
            serializer = EmpleadoSerializer(empleado)
            empleado.delete()
            response = {
                "message" : "registro eliminado",
                "detail" : serializer.data
            }
            return Response(response, status = status.HTTP_200_OK) 
    