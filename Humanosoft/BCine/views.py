from django.http import HttpResponse
from django.shortcuts import render
import aiml #Para usar la app
from .models import PelisDrama,PelisFantasia,PelisFiccion
# Create your views here.

#Sitio principal de BCine

def sitio_principal(request):
    #Realización de una consulta muestra
    return render(request, "Sitio_principal.html")

def pelisDrama(request):
    peliculasD= PelisDrama.objects.all()
    return render(request, "Drama.html",{'peliculasD':peliculasD})

def pelisFantasia(request):
    #Realización de una consulta muestra
    peliculasF= PelisFantasia.objects.all()
    return render(request, "Fantasia.html",{'peliculasF':peliculasF})

def pelisCienciaFiccion(request):
    #Realización de una consulta muestra
    peliculasFC= PelisFiccion.objects.all()
    return render(request, "Ciencia_Ficcion.html",{'peliculasFC':peliculasFC})

def ingresar(request):
        #Realización de una consulta muestra
    botAIML = aiml.Kernel()
    botAIML.learn("./BCine/aiml/startup.aiml")
    botAIML.respond("LOAD AIML BRAIN")
    if request.method =='POST':
        data = request.method('POST')
        user_message =data.get("message", "")

        respuesta = botAIML.respond(user_message.upper())

        if respuesta != "":
            reply = respuesta.capitalize()
        else:
            reply = "No te entendi, lo siento."
        return jsonify({
        "reply": reply,
        "ts": datetime.now().isoformat()
    })
    return render(request,"Chatbot.html",{})

def ver(request):
    return render(request,"DetallesPelicula.html",{})
