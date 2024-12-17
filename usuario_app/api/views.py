from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status
from usuario_app.models import Persona
from .serializers import UsuarioSerializer



class UsuarioAV(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, requets):
        try:
            return Response('Listado de objetos')
        except Persona.DoesNotExist: #excepcion lanzada en caso de no encontrar el campo solicitado
            return Response('')
        
        
class UsuarioDetalleAV(APIView):
    def get(self, request, valor):
        return Response(f'Valor recibido {valor}')