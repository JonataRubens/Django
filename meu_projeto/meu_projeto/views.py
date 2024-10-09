from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.views.generic import ListView
from .models import Carro
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import CarroForm
from django import forms


class ListarCarros(LoginRequiredMixin, ListView):
    model = Carro
    context_object_name = 'veiculos'
    template_name = 'carros.html'
    login_url = '/login/'

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

class CarroUpdateView(UpdateView):
    model = Carro
    form_class = CarroForm
    template_name = 'editar_carro.html'  # Nome do template para exibir o formulário
    context_object_name = 'carro'  # Nome do objeto que será passado para o template
    success_url = reverse_lazy('listar_carros')