from django.db import models

# Create your models here.
class Persona(models.Model):
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True)
    tercer_nombre = models.CharField(max_length=50, blank=True)
    apellido_paterno = models.CharField(max_length=70)
    apellido_materno = models.CharField(max_length=70, blank=True)
    fecha_nacimiento = models.DateField()
    
    class Meta:
        db_table = 'persona'
        verbose_name = 'persona'
        verbose_name_plural = 'personas'