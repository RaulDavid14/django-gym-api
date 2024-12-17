from django.db import models

# Create your models here.
class Persona(models.Model):
    primer_nombre = models.CharField(max_length=255)
    segundo_nombre = models.CharField(max_length=255)
    tercer_nombre = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()

    class Meta:
        db_table = 'persona'
        verbose_name = 'persona'
        verbose_name_plural = 'personas'