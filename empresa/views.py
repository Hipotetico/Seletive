from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Tecnologias, Empresa
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages import constants

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
        tecnologias = request.POST.getlist('tecnologias')
        logo = request.FILES.get('logo')

        if len(nome.strip()) == 0  or len(email.strip()) == 0 or len(cidade.strip()) == 0 or len(endereco.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/home/nova_empresa')

        if logo.size > 100_000_000:
            messages.add_message(request, constants.ERROR, 'Sua logo não pode possuir mais que 10MB')
            return redirect('/home/nova_empresa')

        if nicho not in [i[0] for i in Empresa.choices_nicho_mercado]:
            messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido')
            return redirect('/home/nova_empresa')

        empresa  = Empresa(logo = logo,
                        nome = nome,
                        email = email,
                        cidade = cidade,
                        endereco = endereco,
                        caracteristica_empresa = caracteristicas,
                        nicho_mercado = nicho)

        empresa.save()
        empresa.tecnologia.add(*tecnologias)
        empresa.save()

        messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')

        return redirect("/home/nova_empresa")


def empresas(request):
    tecnologias_filtrar = request.GET.get('tecnologias')
    nome_filtrar = request.GET.get('nome')

    empresas = Empresa.objects.all()
    tecnologias = Tecnologias.objects.all()

    if tecnologias_filtrar:
        empresas = empresas.filter(tecnologia = tecnologias_filtrar)

    if nome_filtrar:
        empresas = empresas.filter(nome__icontains = nome_filtrar)


    return render(request, "empresas.html", {'empresas': empresas ,'tecnologias': tecnologias})


def excluir_empresa(request, id): 
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    messages.add_message(request, constants.SUCCESS, 'Empresa deletada com sucesso')

    return redirect("/home/empresas")

def empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    empresas = Empresa.objects.all()
    tecnologias = Tecnologias.objects.all()
    return render(request, 'empresa.html', {'empresa': empresa, 'tecnologias': tecnologias, 'empresas': empresas})