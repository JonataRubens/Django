from django.contrib import admin
from .models import Carro

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'montadora', 'ano', 'imagem')
    list_filter = ('montadora', 'ano', 'modelo')
