from django.db import models



class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField(default=0)
    descripcion = models.CharField(max_length= 256, default="")
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
# Create your models here.
