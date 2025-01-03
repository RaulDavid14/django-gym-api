from django.db import models
from persona_app.models import Persona  

# Create your models here.
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    jornada = models.IntegerField(verbose_name='jornada laboral')
    usuario = models.CharField(max_length=20)
    ingreso = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'empleado'
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'
        
