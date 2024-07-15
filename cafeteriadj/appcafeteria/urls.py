from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('carrito/', views.carrito, name='carrito'),
    path('cliente/formulario/', views.cliente_formulario, name='cliente_formulario'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
