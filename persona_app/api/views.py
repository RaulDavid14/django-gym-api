from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status
from persona_app.models import Persona
from .serializers import *

#   NombreClaseAv = NombreClaseApiView

class PersonaAV(APIView):  
    def post(self, request):
        serializer = PersonaSerializer(data=request.data)

        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            #hacer algo en caso contrario.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def get(self, requets):
        try:
            if Persona.objects.exists():
                personas = Persona.objects.all()
                serializer = PersonaSerializer(personas, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else :
                return Response({"message": "No hay usuarios disponibles."}, status = status.HTTP_404_NOT_FOUND)
        except Persona.DoesNotExist: #excepcion lanzada en caso de no encontrar el campo solicitado
            return Response({"message": "No hay usuarios disponibles."}, status = status.HTTP_404_NOT_FOUND)
        
        
class PersonaDetalleAV(APIView):
    def __search_by_id(self, id):
        try:
            persona = Persona.objects.get(id_persona = id)
            return persona
        except Persona.DoesNotExist:
            return None
   
    def get(self, request, valor):
        persona = self.__search_by_id(valor)
        if persona is None:
            return Response({"message": "No se encontró el usuario"}, status = status.HTTP_404_NOT_FOUND)
        else:    
            serializer = PersonaSerializer(persona)
            return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, valor):
        persona = self.__search_by_id(valor)
        if persona is None:
            return Response({"message": "No se encontró el registro"}, status = status.HTTP_404_NOT_FOUND)
        else:
            response = {
                "message" : "Se actualizó el registro",
            }        
            serializer = PersonaSerializer(persona, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                response["detail"] = serializer.data
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, valor):
        persona = self.__search_by_id(valor)
        if persona is None:
           return Response({"message": "No se encontró el usuario"}, status = status.HTTP_404_NOT_FOUND)
        else:
            serializer = PersonaSerializer(persona)
            persona.delete()
            response = {
                "message" : "registro eliminado",
                "detail" : serializer.data
            }
            return Response(response, status = status.HTTP_200_OK) 
    