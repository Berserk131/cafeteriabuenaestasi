
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def index(request):
    return render(request, 'index.html')

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
