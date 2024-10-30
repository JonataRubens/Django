# serializers.py
from rest_framework import serializers
from .models import Carro  # Substitua pelo nome correto do seu modelo

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ['id', 'modelo', 'montadora', 'ano', 'imagem']  # ajuste os campos conforme o modelo
