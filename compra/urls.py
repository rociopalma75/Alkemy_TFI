from django.urls import path
from . import views

urlpatterns = [
    path('', views.readProveedores, name="Mostrar como inicio la lista de proveedores"),
    # path('proveedor/registro', views.mostrarCreateProveedor, name="Muestra el form para crear proveedor"),
    path('producto/registro', views.mostrarCreateProducto, name="Muestra el form para crear producto"),
    path('proveedores/', views.readProveedores, name="Muestra todos los proveedores"),
    path('productos/', views.readProductos, name="Mostrar todos los productos"),
    path('proveedor/create', views.proveedorCreate, name="Metodo POST. Crea proveedor"),
    path('producto/create', views.createProducto, name="Metodo POST. Crear producto (sin proveedor)"),
    path('producto/completarCreateProducto', views.completarCreateProducto, name="Metodo POST. Registra el producto con su proveedor"),
    path('producto/<int:idProducto>/proveedor/registro', views.mostrarCreateProveedorParaProducto, name="Mostrar el form de crear proveedor, luego de agregar producto"),
    path('proveedor/eliminar/<int:proveedorId>', views.deleteProveedor, name="Metodo DELETE. Elimina proveedor por id"),
    path('producto/eliminar/<int:productoId>', views.deleteProducto, name="Metodo DELETE. Elimina producto por id"),
    path('producto/editar/<int:productoId>', views.mostrarEditarProducto, name="Mostrar la vista de editar producto por id"),
    path('producto/editar', views.editarProducto, name="Metodo POST. Edita producto"),
]
