# appcafeteria/admin.py
from django.contrib import admin
from .models import Profile, Producto

admin.site.register(Profile)
admin.site.register(Producto)
