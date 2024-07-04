# myapp/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f'{self.user.username} Profile'
