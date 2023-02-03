
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('nova_empresa/', views.nova_empresa, name="nova_empresa"),   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)