from rest_framework import serializers
from utils.validate import Validate
from persona_app.models import Persona

class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = [
            'primer_nombre', 'segundo_nombre', 'tercer_nombre',
            'apellido_paterno', 'apellido_materno', 'fecha_nacimiento'
        ]
        
        extra_kwargs = {
            'id_persona' : {'read_only' : True},
            'primer_nombre': {'validators': [lambda valor: Validate.is_valid_length(3, valor)]},
            'segundo_nombre': {'required': False, 'validators': [lambda valor: Validate.is_valid_length(3, valor)]},
            'tercer_nombre': {'required': False, 'validators': [lambda valor: Validate.is_valid_length(3, valor)]},
            'apellido_paterno': {'validators': [lambda valor: Validate.is_valid_length(5, valor)]},
            'apellido_materno': {'required': False, 'validators': [lambda valor: Validate.is_valid_length(5, valor)]},
            'fecha_nacimiento': {'required': False},
        }
