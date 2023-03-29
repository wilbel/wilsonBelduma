from django.db import models
from pais.models import Pais

# Create your models here.

class Persona(models.Model):
    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=50,blank=True)
    nacimiento = models.DateField()
    nacionalidad = models.ForeignKey(Pais,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
