
from . import views
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('nova_empresa/', views.nova_empresa, name="nova_empresa"),
    path('empresas', views.empresas, name='empresas'),
    path('excluir_empresa/<int:id>', views.excluir_empresa, name='excluir_empresa'),
    path('empresa/<int:id>', views.empresa, name='empresa')   
]