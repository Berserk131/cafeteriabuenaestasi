from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def carrito(request):
    return render(request, 'carrito.html')

def cliente_formulario(request):
    return render(request, 'ClienteFormulario.html')

def login(request):
    return render(request, 'Login.html')

def registro(request):
    return render(request, 'registro.html')