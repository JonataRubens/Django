from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# View para a página inicial (home)
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
            return redirect('test')  # Redireciona para a página desejada após o login
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    
    return render(request, 'login.html')  # Renderiza a tela de login


def home(request):
    return render(request, 'home.html')  # Página protegida, só acessível após login

def logout_view(request):
    logout(request)
    return redirect('login')