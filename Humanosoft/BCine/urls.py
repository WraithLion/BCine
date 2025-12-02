from django.urls import path
from . import views
# Nombre de la aplicación
app_name = 'BCine'
#Registro de los enlaces de navegacion a las diferentes paginas de BCine
urlpatterns = [

# Página principal de cine

path('', views.sitio_principal, name='sitio_principal'),

# Página para mostrar peliculas de género Drama

path('BCine/Drama/',views.pelisDrama,name='sitio_drama'),

# Página para mostrar peliculas de género Drama

path('BCine/Fantasia/',views.pelisFantasia,name='sitio_fantasia'),

# Página para mostrar peliculas de género Fantasía

path('BCine/Ciencia-Ficcion/',views.pelisCienciaFiccion,name='sitio_ciencia_ficcion'),

# Página para mostrar peliculas de género Ciencia Ficccion

path('BCine/Cuenta/',views.ingresar,name='chatbot'),

# Página para mostrar detalles de la pelicula seleccionada por el usuario

path('BCine/ver/',views.ver,name='Detalles_Pelicula'),

# Direccion api

path('api/message',views.ingresar, name='chatbot'),


]
