from django.urls import path
from . import views

urlpatterns = [
    path('', views.readProveedores, name="Mostrar como inicio la lista de proveedores"),
    path('proveedor/registro', views.mostrarCreateProveedor),
    path('proveedores/', views.readProveedores, name="Muestra todos los proveedores"),
    path('productos/', views.readProductos, name="Mostrar todos los productos"),
    path('proveedor/create', views.createProveedor, name="Crear proveedor nuevo"),
    path('createProveedor/<str:nombre>/<str:apellido>/<int:dni>', views.createProveedorv2, name="Crear nuevo proveedor"),
]
