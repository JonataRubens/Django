from django.contrib import admin
from django.urls import include, path 
from .views import CarroUpdateView, CarroViewSet, ListarCarros, adicionar_carro, exclusao_carro, login_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'carros', CarroViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', login_view, name='/login/'),
    path('', ListarCarros.as_view(), name='listar_carros'),
    path('<int:pk>/', CarroUpdateView.as_view(), name='editar_carro'),
    path('carro/<int:carro_id>/excluir/', exclusao_carro, name='excluir_carro'),
    path('add/', adicionar_carro, name='adicionar_carro'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    
    path('api/', include(router.urls)),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
