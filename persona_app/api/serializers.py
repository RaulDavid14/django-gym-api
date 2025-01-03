from rest_framework import serializers
from persona_app.models import Persona  

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id_persona', 'primer_nombre', 'segundo_nombre', 'tercer_nombre', 
                  'apellido_paterno', 'apellido_materno', 'fecha_nacimiento']
        
        extra_kwargs = {
            'id_persona': {'read_only': True},  
        }