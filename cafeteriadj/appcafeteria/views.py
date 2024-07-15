from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Producto  # Asegúrate de importar el modelo

def index(request):
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'index.html', {'productos': productos})  # Pasa los productos al contexto

def carrito(request):
    return render(request, 'carrito.html')

def cliente_formulario(request):
    return render(request, 'ClienteFormulario.html')

def login(request):
    return render(request, 'Login.html')

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            return redirect('login')  # Cambia 'login' por el nombre de tu vista de inicio de sesión
    else:
        form = UserRegisterForm()
    return render(request, 'registro.html', {'form': form})
