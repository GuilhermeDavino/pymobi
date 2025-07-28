from django.http import HttpResponse
from django.shortcuts import render
from .models import Imovel
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/logar/')
def home(request):
    imoveis = Imovel.objects.all()
    return render(request, 'home/home.html', {'imoveis': imoveis})
