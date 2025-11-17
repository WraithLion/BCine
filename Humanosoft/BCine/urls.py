from django.urls import path
from . import views
# Nombre de la aplicación
app_name = 'BCine'
urlpatterns = [
# Página principal de la tiendita
path('', views.index, name='index'),
path('productos/',views.todosproductos,name='todos-los-productos'),
path('productosNoIA/',views.todosproductosNoIA,name='todos-los-productos-sin-IA'),
]
