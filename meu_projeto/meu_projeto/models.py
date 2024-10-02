OPCOES_MARCAS = (
    ('1', 'AUDI'),
    ('2', 'BMW'),
    ('3', 'CHEVROLET - GM'),
    ('4', 'FIAT'),
    ('5', 'FORD'),
    ('6', 'HONDA'),
    ('7', 'HYUNDAI'),
    ('8', 'VOLKSWAGEN'),
)
 
OPCOES_CORES = (
    ('1', 'BRANCO'),
    ('2', 'AMARELO'),
    ('3', 'AZUL'),
    ('4', 'PRATA'),
    ('5', 'PRETO'),
    ('6', 'VERMELHO'),
)

from django.db import models

class Carro(models.Model):
    montadora = models.CharField(max_length=50, choices=OPCOES_MARCAS)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    cor = models.CharField(max_length=50, choices=OPCOES_CORES)

    def __str__(self):
        return f'{self.montadora} {self.modelo} ({self.ano})'
    
    
