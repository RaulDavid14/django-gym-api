from rest_framework import serializers
from empleado_app.models import Empleado  # Modelo de empleado de esta app
from persona_app.api.serializers import PersonaSerializer  # Importa el serializador de Persona

class EmpleadoSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer()  # Usa el serializador anidado

    class Meta:
        model = Empleado
        fields = ['id_empleado', 'persona', 'jornada', 'usuario']

        extra_kwargs = {
            'id_empleado': {'read_only': True}, 
            'ingreso': {'read_only': True}
        }

    def create(self, validated_data):
        # Extraer datos de persona
        persona_data = validated_data.pop('persona')
        # Crear la instancia de Persona
        from persona_app.models import Persona  # Importa el modelo si no está al inicio
        persona = Persona.objects.create(**persona_data)
        # Crear la instancia de Empleado asociada
        empleado = Empleado.objects.create(persona=persona, **validated_data)
        return empleado
