from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Carro


def home(request):
    return render(request, 'home.html') 

def test(request):
    return render(request, 'test.html')

def youname(request, name):
    return render(request, 'youname.html', {'name': name})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Usando o login do Django
            return redirect('/carros/')  # Redireciona para a página desejada após o login
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    
    return render(request, 'login.html')  # Renderiza a tela de login


class ListarCarros(ListView):
    model = Carro
    template_name = 'carros.html'
    context_object_name = 'veiculos'

