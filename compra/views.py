from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proveedor, Producto

# Create your views here.
def mostrarCreateProveedorParaProducto(request, idProducto):
    return render(request, 'crear_proveedor.html',{'idProducto': idProducto})

def mostrarEditarProducto(request, productoId):
    producto = Producto.objects.get(id=productoId)
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, 'editar_producto.html', {'p': producto,'productos':productos, 'proveedores':proveedores})

def readProveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

def readProductos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def createProveedor(request):
    if request.method == 'POST':
        prov = Proveedor()
        prov.nombre = request.POST['nombre']
        prov.apellido = request.POST['apellido']
        prov.dni = request.POST['dni']

        try:
            prov.full_clean()
        except Exception as e:
            print("Excepcion:" , e)
            return render(request, 'crear_proveedor.html', {'e' : e})

        prov.save()
        try:
            if request.POST['idProducto'] is not None:
                idProducto = request.POST['idProducto']
                producto = Producto.objects.get(id=idProducto)
                proveedores = Proveedor.objects.all()
                return render(request, 'agregar_proveedor.html', {'producto': producto, 'proveedores': proveedores})
        except:    
            return render(request, 'crear_proveedor.html', {'proveedor': prov})
    else: # Metodo GET
        return render(request, 'crear_proveedor.html')


def createProducto(request):
    if request.method == 'POST':
        prod = Producto()
        prod.nombre = request.POST['nombre']
        prod.precio = request.POST['precio']
        prod.stock_actual = request.POST['stock_actual']
        prod.proveedor = None

        try:
            prod.full_clean()
        except Exception as e:
            print("Excepcion: ", e)
            return render(request, 'crear_producto.html',{'e':e})
        
        prod.save()
        proveedores = Proveedor.objects.all()
        return render(request, 'agregar_proveedor.html', {'producto': prod, 'proveedores': proveedores})
    else: #Metodo GET
        return render(request, 'crear_producto.html')
    
def agregarProveedorAProducto(request): 
    productoId = request.POST['id']
    proveedorId = request.POST['proveedor']
    proveedor = Proveedor.objects.get(id=proveedorId)
    producto = Producto.objects.get(id=productoId)
    producto.proveedor = proveedor
    producto.save()

    return render(request, 'crear_producto.html',{'producto': producto})

def deleteProveedor(request, proveedorId):
    proveedor = Proveedor.objects.get(id=proveedorId)
    proveedor.delete()
    return redirect('/')

def deleteProducto(request, productoId):
    producto = Producto.objects.get(id=productoId)
    producto.delete()
    return redirect('/productos')

def editarProducto(request):
    if request.method == 'POST':
        productoId = request.POST['idProducto']
        producto = Producto.objects.get(id=productoId)
        producto.nombre = request.POST['nombre']
        producto.precio = request.POST['precio']
        producto.stock_actual = request.POST['stock_actual']
        if request.POST['proveedor']:
            proveedorId = request.POST['proveedor']
            proveedor = Proveedor.objects.get(id = proveedorId)
            producto.proveedor = proveedor
        producto.save()
    
    return redirect('/productos')


