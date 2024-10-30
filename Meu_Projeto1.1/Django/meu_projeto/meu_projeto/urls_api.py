from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarroViewSet

# Defina o roteador e registre a view de carros
router = DefaultRouter()
router.register(r'carros', CarroViewSet)

listar_carros = CarroViewSet.as_view({'get': 'list'})
criar_carro = CarroViewSet.as_view({'post': 'create'})
detalhe_carro = CarroViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

# Inclua as rotas do roteador em urlpatterns
urlpatterns = [
    path('api/carros/', listar_carros, name='listar_carros'),  # Rota para listar carros
    path('api/carros/novo/', criar_carro, name='criar_carro'),  # Rota para criar um carro
    path('api/carros/<int:pk>/', detalhe_carro, name='detalhe_carro'),
]