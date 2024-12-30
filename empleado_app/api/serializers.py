from rest_framework import serializers
from utils import validate
from empleado_app.models import Empleado


class EmpleadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Empleado
        fields = ['persona','jornada','usuario']
        
        extra_kwargs = {
            'id_empleado' : {'read_only' : True},
            'ingreso' : {'read_only' : True}
        }