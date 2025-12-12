from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Usuario

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')

        # Validações
        if not all([nome, cpf, telefone, email, senha, senha2]):
            messages.error(request, 'Todos os campos são obrigatórios!')
            return render(request, 'cadastro/cadastro.html')
        
        if senha != senha2:
            messages.error(request, 'As senhas não conferem!')
            return render(request, 'cadastro/cadastro.html')
        
        if Usuario.objects.filter(cpf=cpf).exists():
            messages.error(request, 'CPF já cadastrado!')
            return render(request, 'cadastro/cadastro.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado!')
            return render(request, 'cadastro/cadastro.html')

        # Criar usuário Django
        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=senha,
                first_name=nome.split()[0],
                last_name=' '.join(nome.split()[1:])
            )
            # Criar perfil adicional
            Usuario.objects.create(
                user=user,
                cpf=cpf,
                telefone=telefone
            )
            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar: {str(e)}')
            return render(request, 'cadastro/cadastro.html')
    
    return render(request, 'cadastro/cadastro.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        try:
            user = authenticate(request, username=email, password=senha)
            if user is not None:
                auth_login(request, user)
                request.session['show_welcome'] = True
                return redirect('index')
            else:
                messages.error(request, 'Email ou senha inválidos!')
        except Exception as e:
            messages.error(request, f'Erro ao fazer login: {str(e)}')
    
    return render(request, 'cadastro/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Você foi desconectado.')
    return redirect('login')

def index(request):
    if request.user.is_authenticated:
        usuario = Usuario.objects.filter(user=request.user).first()
        # show welcome once after login
        if request.session.pop('show_welcome', False):
            messages.success(request, f'Bem-vindo, {request.user.first_name}!')
        context = {
            'usuario': usuario,
            'nome_usuario': request.user.first_name or request.user.username,
        }
    else:
        context = {}
    return render(request, 'cadastro/index.html', context)

def eventos(request):
    return render(request, 'cadastro/eventos.html')

def faq(request):
    return render(request, 'cadastro/faq.html')

def feed(request):
    return render(request, 'cadastro/feed.html')

def guias(request):
    return render(request, 'cadastro/guias.html')

def home_off(request):
    return render(request, 'cadastro/home_off.html')

def parcerias(request):
    return render(request, 'cadastro/parcerias.html')