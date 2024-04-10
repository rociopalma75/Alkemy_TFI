from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
    def clean(self): #Validaciones de cada campo
        if not self.nombre.isalpha():
            for caracter in self.nombre:
                if not caracter.isalpha() and not caracter.isspace():
                    raise ValidationError('nombreInvalido')

        if not self.apellido.isalpha():
            for caracter in self.apellido:
                if not caracter.isalpha() and not caracter.isspace():
                    raise ValidationError('apellidoInvalido')
        
        if len(str(self.dni)) <= 7 or len(str(self.dni)) >= 10: # Validacion muy manual
            raise ValidationError('dniInvalido')
    
    class Meta:
        ordering=['id','apellido', 'nombre'] # Orden asc en apellido y nombre
        verbose_name_plural = 'Proveedores'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    def clean(self):
        if not self.nombre.isalpha():
            for caracter in self.nombre:
                if not caracter.isalpha() and not caracter.isspace():
                    raise ValidationError('nombreInvalido')
    
    class Meta:
        ordering=['nombre', '-stock_actual'] #Orden asc en nombre y desc en stock
        verbose_name_plural = 'Productos'    