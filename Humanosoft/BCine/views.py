from django.http import HttpResponse
from django.shortcuts import render
import aiml #Para usar la app
from django.http import JsonResponse
from datetime import datetime
import json
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import PelisDrama, PelisFantasia, PelisFiccion   #Importa los modelos con los datos de cada Género de pelicula - Drama   Fantasia    Ciencia Ficcion
# Create your views here.

#Sitio principal de BCine

def sitio_principal(request):
    #Renderiza la página principal de BCine
    return render(request, "Sitio_principal.html")

#Sitio para género de peliculas Drama

def pelisDrama(request):
    #Realiza una consulta para cargar todas las peliculas y mostrar en la pagina
    peliculasD= PelisDrama.objects.all()
    return render(request, "Drama.html",{'peliculasD':peliculasD})

#Sitio para género de peliculas Fantasia

def pelisFantasia(request):
    #Realiza una consulta para cargar todas las peliculas y mostrar en la pagina
    peliculasF= PelisFantasia.objects.all()
    return render(request, "Fantasia.html",{'peliculasF':peliculasF})

#Sitio para género de peliculas Ciencia Ficcion

def pelisCienciaFiccion(request):
    #Realiza una consulta para cargar todas las peliculas y mostrar en la pagina
    peliculasFC= PelisFiccion.objects.all()
    return render(request, "Ciencia_Ficcion.html",{'peliculasFC':peliculasFC})

    #Realización de una consulta muestra
botAIML = aiml.Kernel()
botAIML.learn("./BCine/aiml/startup.aiml") #Ruta del archivo aiml para inicializar el Chatbot
botAIML.respond("LOAD AIML BRAIN") #Carga sus datos de conocimiento

#Sitio para Cuenta e interaccion con chatbot
@ensure_csrf_cookie
def ingresar(request):
    if request.method =='POST': #Realiza una petición para responder
        data = json.loads(request.body)
        user_message = data.get("message", "") #Lee la respuesta ingresada del usuario

        respuesta = botAIML.respond(user_message.upper()) #Analiza el mensaje para emitir una respuesta adecuada

        if respuesta != "":
            reply = respuesta.capitalize() #En caso de encontrar la respuesta a su peticion responde con un mensaje con la información
        else:
            reply = "No te entendi, lo siento." #En caso contrario mostrará un mensaje de no entendimiento
        return JsonResponse({
        "reply": reply,     #Devuelve el mensaje en formato respuesta
        "ts": datetime.now().isoformat() #Acompaña la respuesta con la hora en que fue emitido
    })
    return render(request,"Chatbot.html",)    #Renderiza la pagina para interactuar con el chatbot

#Sitio para mostrar de la pelicula seleccionada por el usuario
#Ver pelicula
#Escribir una reseña
#Valorar con una puntuación en estrellas

def ver(request):
    return render(request,"VerPelicula.html",{})
