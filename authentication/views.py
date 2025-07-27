from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.messages import constants 

# Create your views here.

def auth(request):
    return HttpResponse("Pegou a view de autenticação")

def logar(request):
    
    return HttpResponse("Login view")

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro/cadastro.html')
    elif request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha =  request.POST.get('senha')

        if(len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos!')
            return redirect('/auth/cadastro')
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe!')
            return redirect('/auth/cadastro')
        
        try:
            user = User(username=username, email=email, password=senha)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!')
            return redirect('/auth/logar')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema ao cadastrar usuário!')
            return redirect('/auth/cadastro')
    
    
    
