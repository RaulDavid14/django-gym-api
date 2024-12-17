from rest_framework import serializers
from utils.validate import Validate

class UsuarioSerializer(serializers.Serializer):
    id_persona = serializers.IntegerField(read_only=True)
    
    primer_nombre = serializers.CharField(max_length=255, validators=[
        lambda valor : Validate.is_valid_length(3, valor)
    ])
    segundo_nombre = serializers.CharField(max_length=255, required=False, validators=[
        lambda valor : Validate.is_valid_length(3, valor)
    ])
    tercer_nombre = serializers.CharField(max_length=255, required=False, validators=[
        lambda valor : Validate.is_valid_length(3, valor)
    ])
    apellido_paterno = serializers.CharField(max_length=255, validators = [
        lambda valor : Validate.is_valid_length(5,valor)
    ])
    apellido_materno = serializers.CharField(max_length=255, required=False, validators = [
        lambda valor : Validate.is_valid_length(5,valor)
    ])
    fecha_nacimiento = serializers.DateField(required=False)
