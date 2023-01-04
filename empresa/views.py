from django.http import HttpResponse
from django.shortcuts import render
from .models import Tecnologias, Empresa

# Create your views here.

def nova_empresa(response):
    techs = Tecnologias.objects.all()
    nichos = Empresa.choices_nicho_mercado
    
    return render(response, 'nova_empresa.html', {'techs': techs, 'nichos': nichos})