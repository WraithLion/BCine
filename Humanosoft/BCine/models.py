from django.db import models

# Create your models here.

class PelisFiccion(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(null=True)
    director = models.CharField(max_length=25,null=True)
    descripcion = models.TextField(blank=True)
    def __str__(self):
        return f"{self.nombre} - {self.director}"

class PelisDrama(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(null=True)
    director = models.CharField(max_length=25,null=True)
    descripcion = models.TextField(blank=True)
    def __str__(self):
        return f"{self.nombre} - {self.director}"

class PelisFantasia(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(null=True)
    director = models.CharField(max_length=25,null=True)
    descripcion = models.TextField(blank=True)
    def __str__(self):
        return f"{self.nombre} - {self.director}"

class Usuarios(models.Model):
    nombre = models.CharField(max_length=35)
    contraseña=models.CharField(max_length=12)
    def __str__(self):
        return f"{self.nombre} - {self.contraseña}"
