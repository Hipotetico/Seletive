
from . import views
from django.urls import path

urlpatterns = [
    path('nova_empresa/', views.nova_empresa, name="nova_empresa")
     
]
