from django.db import models
from django.utils import timezone

# Create your models here.

class contacto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre
    
class ak47(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to = "ak47", null=True)
    def __str__(self):
        return self.nombre
    
class m4a1(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to = "m4a1", null=True)
    def __str__(self):
        return self.nombre
    
class awp(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to = "awp", null=True)
    def __str__(self):
        return self.nombre
    
    
