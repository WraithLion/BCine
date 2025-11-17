from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    descripcion = models.TextField(blank=True)
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
class Ulthwe(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    precio = models.DecimalField(
    max_digits=8,
    decimal_places=2
    )
    def __str__(self):
        return f"Ulthwe {self.nombre} ({self.color})"
