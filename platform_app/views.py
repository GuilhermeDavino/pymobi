from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Imovel, Cidade, Visitas
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required(login_url='/auth/logar/')
def home(request):

    preco_minimo = request.GET.get('preco_minimo')
    preco_maximo = request.GET.get('preco_maximo')
    cidade = request.GET.get('cidade')
    tipo = request.GET.getlist('tipo')
    
    if preco_maximo or preco_minimo or cidade or tipo:
        
        if not preco_minimo:
            preco_minimo = 0
        
        if not preco_maximo:
            preco_maximo = 9999999999
        
        if not tipo:
            tipo = ['A', 'C']

        imoveis = Imovel.objects.filter(valor__gte=preco_minimo).filter(valor__lte=preco_maximo).filter(tipo_imovel__in=tipo).filter(cidade=cidade)
    else:
        imoveis = Imovel.objects.all()
    
    cidades = Cidade.objects.all()
    return render(request, 'home/home.html', {'imoveis': imoveis, 'cidades': cidades})


def imovel(request, id):
    imovel = get_object_or_404(Imovel, id=id)
    sugestoes = Imovel.objects.filter(cidade=imovel.cidade).exclude(id=id)[:2]
    return render(request, 'imovel/imovel.html', {'imovel': imovel, 'sugestoes': sugestoes})


def agendar_visitas(request):
    usuario = request.user
    dia = request.POST.get('dia')
    horario = request.POST.get('horario')
    id_imovel = request.POST.get('id_imovel')
    visitas = Visitas(
        imovel_id = id_imovel,
        usuario = usuario,
        dia = dia,
        horario = horario
    )
    visitas.save()
    return redirect('/agendamentos')

def agendamentos(request):
    visitas = Visitas.objects.filter(usuario=request.user)
    return render(request, 'agendamentos/agendamentos.html', {'visitas': visitas})


def cancelar_agendamento(request, id):
    visitas = get_object_or_404(Visitas, id=id)
    visitas.status = "C"
    visitas.save()
    return redirect('/agendamentos')