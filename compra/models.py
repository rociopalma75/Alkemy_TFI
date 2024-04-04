from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
    class Meta:
        ordering=['id','apellido', 'nombre'] # Orden asc en apellido y nombre
        verbose_name_plural = 'Proveedores'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering=['nombre', '-stock_actual'] #Orden asc en nombre y desc en stock
        verbose_name_plural = 'Productos'
