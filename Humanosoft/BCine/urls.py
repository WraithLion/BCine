from django.urls import path
from . import views
# Nombre de la aplicación
app_name = 'BCine'
urlpatterns = [
# Página principal de cine
path('BCine/', views.sitio_principal, name='sitio_principal'),


path('BCine/Drama/',views.pelisDrama,name='sitio_drama'),

path('BCine/Fantasia/',views.pelisFantasia,name='sitio_fantasia'),


path('BCine/Ciencia-Ficcion/',views.pelisCienciaFiccion,name='sitio_ciencia_ficcion'),

path('BCine/Cuenta/',views.ingresar,name='chatbot'),

path('ver/',views.ver,name='Detalles_Pelicula'),


]
