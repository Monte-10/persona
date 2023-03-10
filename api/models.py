from django.db import models

# Create your models here.
# Persona con estructura persona(id, nombre, apellido, email)
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    
    class Meta:
        ordering = ['id']