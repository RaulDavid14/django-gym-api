from django.db import models

# Create your models here.
class Empleado(models.Model):
    persona = models.OneToOneField("persona_app.Persona", verbose_name="persona", on_delete=models.CASCADE)
    jornada = models.IntegerField(verbose_name='jornada laboral')
    # perfil
    usuario = models.CharField(max_length=20)
    ingreso = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'empleado'
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'