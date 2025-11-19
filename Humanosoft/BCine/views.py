from django.http import HttpResponse
from django.shortcuts import render
from .models import PelisDrama,PelisFantasia,PelisFiccion
# Create your views here.

#Sitio principal de BCine

def sitio_principal(request):
    #Realización de una consulta muestra
    peliculasD= PelisDrama.objects.all()
    return render(request, "sitio_principal.html",{'peliculasD':peliculasD})

def todosproductos(request):
    #Realización de una consulta muestra
    peliculasF= PelisFantasia.objects.all()
    return render(request, "todos-los-productos.html",{'peliculasF':peliculasF})

def todosproductosNoIA(request):
    #Realización de una consulta muestra
    peliculasFC= PelisFiccion.objects.all()
    return render(request, "todos-los-productos-sin-IA.html",{'peliculasFC':peliculasFC})
def ingresar(request):
    return render(request,"chatbot.html",{})
def ver(request):
    return render(request,"DetallesPelicula.html",{})
