from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_mediano = models.DecimalField(max_digits=6, decimal_places=2)
    precio_grande = models.DecimalField(max_digits=6, decimal_places=2)
    imagen= models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre