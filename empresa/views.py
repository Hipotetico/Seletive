from django.http import HttpResponse
from django.shortcuts import render
from .models import Tecnologias, Empresa

# Create your views here.

def nova_empresa(request):
    if request.method == 'GET':
        techs = Tecnologias.objects.all()
        nichos = Empresa.choices_nicho_mercado
        
        return render(request, 'nova_empresa.html', {'techs': techs, 'nichos': nichos})

    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        endereco = request.POST.get('endereco')
        nicho = request.POST.get('nicho')
        caracteristicas = request.POST.get('caracteristicas')
        
        return HttpResponse('Teste')