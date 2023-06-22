from django.shortcuts import render
from .models import Aluno

def home(request):
    alunos = Aluno.objects.all()
    context = {'alunos': alunos}
    return render(request, 'index.html', context)

def aluno_list(request, id):
    alunos = Aluno.objects.get(id=id)
    context = {'aluno': alunos}
    return render(request, 'aluno_list.html', context)

from django.shortcuts import render

def contato(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        mensagem = request.POST['mensagem']
        
        print(f'Nome: {nome}')
        print(f'Email: {email}')
        print(f'Mensagem: {mensagem}')
        
        return render(request, 'contato.html')

    return render(request, 'contato.html')