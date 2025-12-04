from django.http import HttpResponse
from django.shortcuts import render
import aiml #Para usar la app
from django.http import JsonResponse
from datetime import datetime
import json
import os
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

MEMORY_FILE="memoriaBot.json"
    #Realización de una consulta muestra
botAIML = aiml.Kernel()
botAIML.learn("./BCine/aiml/startup.aiml") #Ruta del archivo aiml para inicializar el Chatbot
botAIML.respond("LOAD AIML BRAIN") #Carga sus datos de conocimiento

# FUNCIONES DE MEMORIA PARA EL CHATBOT - CINE-B


#Funcion para cargar los datos recopilados del usuario
def cargarMem_Usuario(usuario_id):
    if os.path.exists(MEMORY_FILE): #Verifica la existencia del archivo
        try:
            with open(MEMORY_FILE, 'r', encoding='utf-8') as f: #Realiza la lectura del archivo
                memoriasTodas = json.load(f)    #Carga el archivo .json
                return memoriasTodas.get(usuario_id,{})    #Carga el identificador el usuario
        except:
            return {}   #Devuelve un diccionario vacío de id de usuarios
    return {}

#Funcion que resguarda los datos de un usuario en particular

def guardar_Mem_Usuario(usuario_id,archivoMemoria):
    #Almacena los datos del usuario
    memoriasTodas={}

    # Cargar memorias existentes de un archivo json.
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE,'r',encoding='utf-8') as f:
                memoriasTodas=json.load(f)
        except:
            memoriasTodas={}

    memoriasTodas[usuario_id]=archivoMemoria

    #Almacena los datos del usuario en un archivo JSON

    with open(MEMORY_FILE, 'w',encoding='utf-8') as f:
        json.dump(memoriasTodas,f,indent=2,ensure_ascii=False)

def restaurar_aiml(datosMem):

    #Variable que reinicia las variables del bot AIML

    for key,value in datosMem.items():
        botAIML.setPredicate(key,value)


#Funcion que extrae las variables del bot AIML actuales

def extraer_aiml():

    #Campos a recopilar del usuario

    predicates_to_save=['usuario','contraseña']
    memoria={}

    for pred in predicates_to_save:
        campo= botAIML.getPredicate(pred)
        if campo and campo !='unknown':
            memoria[pred]=campo

    return memoria

#Sitio para Cuenta e interaccion con chatbot
@ensure_csrf_cookie
def ingresar(request):
    if 'usuario_id' not in request.session:
            request.session['usuario_id'] = os.urandom(16).hex()
    usuario_id = request.session.get('usuario_id', 'default')
    if request.method =='POST': #Realiza una petición para responder

        data = json.loads(request.body)

        user_message = data.get("message", "") #Lee la respuesta ingresada del usuario
         #Identificador del usuario

        memoria_usuario= cargarMem_Usuario(usuario_id) # Carga los datos del usuario

        restaurar_aiml(memoria_usuario) #Recupera los campos en AIML

        respuesta = botAIML.respond(user_message.upper()) #Analiza el mensaje para emitir una respuesta adecuada

        if respuesta != "":
            reply = respuesta.capitalize() #En caso de encontrar la respuesta a su peticion responde con un mensaje con la información
        else:
            reply = "No te entendi, lo siento." #En caso contrario mostrará un mensaje de no entendimiento

        #Proceso para extrer y almacenar las nuevas variables capturadas
        memoria_actualizada= extraer_aiml()
        guardar_Mem_Usuario(usuario_id,memoria_actualizada)

        return JsonResponse({
        "reply": reply,     #Devuelve el mensaje en formato respuesta
        "ts": datetime.now().isoformat(),
        "memoria":memoria_actualizada   #Acompaña la respuesta con la hora en que fue emitido
    })
    return render(request,"Chatbot.html",{'usuario_id': usuario_id})    #Renderiza la pagina para interactuar con el chatbot

#Sitio para mostrar de la pelicula seleccionada por el usuario
#Ver pelicula
#Escribir una reseña
#Valorar con una puntuación en estrellas

def ver(request):
    return render(request,"VerPelicula.html",{})
