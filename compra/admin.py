from django.contrib import admin
from .models import Proveedor, Producto
# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
    list_display=['apellido', 'nombre', 'dni']

class ProductoAdmin(admin.ModelAdmin):
    list_display=['nombre','precio','stock_actual','proveedor']


admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)