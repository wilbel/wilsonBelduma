from django.db import models

# Create your models here.

class Pais(models.Model):
        nombre = models.CharField(max_length=30,unique=True)
        nacionalidad = models.CharField(max_length=50, blank=True)
    

        def __str__(self):
                return self.nombre
