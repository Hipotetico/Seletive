from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def nova_empresa(response):
    return render(response, 'nova_empresa.html')