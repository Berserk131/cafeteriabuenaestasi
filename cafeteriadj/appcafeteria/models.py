from django.db import models
from django.contrib.auth.models import User

# Modelo de Perfil del usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f'{self.user.username} Profile'

# Modelo de Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre
