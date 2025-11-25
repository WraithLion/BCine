from django.db import models

# Modelos a utilizar para el sitio:
# Genero de pelicula
# Usuarios (nuevos y existentes)

#Modelo para almacenar peliculas de género Ciencia Ficcion

class PelisFiccion(models.Model):
    nombre = models.CharField(max_length=100)   #Nombre de la pelicula
    imagen = models.ImageField(null=True)   #Imagen de la pelicula en cartelera
    director = models.CharField(max_length=25,null=True) # Nombre del director
    descripcion = models.TextField(blank=True)  #Descripcion breve de la pelicula
    def __str__(self):
        return f"{self.nombre} - {self.director}"   #Muestra la informacion necesaria de la pelicula dados los aspectos anteriores

#Modelo para almacenar peliculas de género Drama

class PelisDrama(models.Model):
    nombre = models.CharField(max_length=100)   #Nombre de la pelicula
    imagen = models.ImageField(null=True)   #Imagen de la pelicula en cartelera
    director = models.CharField(max_length=25,null=True) # Nombre del director
    descripcion = models.TextField(blank=True)  #Descripcion breve de la pelicula
    def __str__(self):
        return f"{self.nombre} - {self.director}"   #Muestra la informacion necesaria de la pelicula dados los aspectos anteriores

#Modelo para almacenar peliculas de género Fantasia

class PelisFantasia(models.Model):
    nombre = models.CharField(max_length=100)   #Nombre de la pelicula
    imagen = models.ImageField(null=True)   #Imagen de la pelicula en cartelera
    director = models.CharField(max_length=25,null=True) # Nombre del director
    descripcion = models.TextField(blank=True)  #Descripcion breve de la pelicula
    def __str__(self):
        return f"{self.nombre} - {self.director}"   #Muestra la informacion necesaria de la pelicula dados los aspectos anteriores

#Modelo para almacenar datos de usuario

class Usuarios(models.Model):
    nombre = models.CharField(max_length=35)    #Nombre de usuario
    contraseña=models.CharField(max_length=12)  #Contraseña
    def __str__(self):
        return f"{self.nombre} - {self.contraseña}" #Devuelve la informacion del usuario
