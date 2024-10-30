from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Carro
from .forms import CarroForm
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import CarroSerializer

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
            auth_login(request, user)
            return redirect('/carros/')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    
    return render(request, 'login.html')

class CarroUpdateView(UpdateView):
    model = Carro
    form_class = CarroForm
    template_name = 'editar_carro.html'
    context_object_name = 'carro'
    success_url = reverse_lazy('listar_carros')

def exclusao_carro(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    
    if request.method == 'POST':
        carro.delete()
        return redirect('listar_carros')
    
    return redirect('listar_carros')

def adicionar_carro(request):
    if request.method == 'POST':
        form = CarroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_carros')
    else:
        form = CarroForm()
    
    return render(request, 'add_car.html', {'form': form})




class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer