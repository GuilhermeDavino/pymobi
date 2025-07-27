from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def auth(request):
    return HttpResponse("Pegou a view de autenticação")
