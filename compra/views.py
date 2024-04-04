from django.shortcuts import render
from django.http import HttpResponse
from .models import Proveedor, Producto
from django.template import Template, Context

# Create your views here.
def mostrarCreateProveedor(request):
    return render(request, 'crear_proveedor.html')

def createProveedor(request):
    if request.method == 'POST':
        prov = Proveedor()
        prov.nombre = request.POST['nombre']
        prov.apellido = request.POST['apellido']
        prov.dni = request.POST['dni']
        prov.save()
    
        return render(request, 'crear_proveedor.html', {'proveedor': prov})

def createProveedorv2(request, nombre, apellido, dni):
    nuevo_proveedor = Proveedor.objects.create(
        nombre = nombre,
        apellido = apellido,
        dni = dni
    )
    ruta = "C:\\Users\\rocio\\OneDrive\\Documentos\\Alkemy-Trabajo_Integrador_Individual\\StockControl\\compra\\templates\\nuevo_proveedor.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({'proveedor' : nuevo_proveedor})
    return HttpResponse(plantilla.render(contexto))

def readProveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

def deleteProveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores', {'proveedores': proveedores})

def readProductos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})