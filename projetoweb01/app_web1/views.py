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