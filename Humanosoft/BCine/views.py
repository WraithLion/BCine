from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto, Ulthwe
# Create your views here.

#Sitio principal de BCine

def sitio_principal(request):
    #Realización de una consulta muestra
    producto1= Ulthwe.objects.get(nombre='Original',
                                  color='Rosa pastel')
    return render(request, "sitio_principal.html",{'producto1':producto1})

def todosproductos(request):
    #Realización de una consulta muestra
    todos_productos= Producto.objects.all()
    return render(request, "todos-los-productos.html",{'todos_productos':todos_productos})

def todosproductosNoIA(request):
    #Realización de una consulta muestra
    todos_productos= Producto.objects.all()
    return render(request, "todos-los-productos-sin-IA.html",{'todos_productos':todos_productos})
