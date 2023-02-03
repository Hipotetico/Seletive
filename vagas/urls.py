
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('nova_vaga/', views.nova_vaga, name="nova_vaga"),   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)