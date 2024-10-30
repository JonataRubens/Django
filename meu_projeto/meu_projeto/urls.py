from . import views
from django.contrib import admin
from django.urls import path 
from .views import CarroUpdateView, ListarCarros, adicionar_carro, exclusao_carro, login_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='/login/'),
    path('carros/', ListarCarros.as_view(), name='listar_carros'),
    path('<int:pk>/', CarroUpdateView.as_view(), name='editar_carro'),
    path('carro/<int:carro_id>/excluir/', exclusao_carro, name='excluir_carro'),
    path('add/', adicionar_carro, name='adicionar_carro'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
