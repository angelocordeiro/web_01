from django.shortcuts import render

def home(request):
  return render(request,"index.html")

def aluno2(request):
  return render(request,"aluno2.html")

def aluno_list(request):
    alunos = [
        {'nome': 'Fulano de Matos', 'periodo_ingresso': '1/2023', 'nota_web': 75, 'situacao': 'Aprovado'},
        {'nome': 'Sicrano de Souza', 'periodo_ingresso': '1/2022', 'nota_web': 85, 'situacao': 'Aprovado'},
        {'nome': 'Mateus Martiniano', 'periodo_ingresso': '2/2022', 'nota_web': 90, 'situacao': 'Aprovado'},
        {'nome': 'Evandra Sales', 'periodo_ingresso': '2/2023', 'nota_web': 60, 'situacao': 'Reprovado'},
    ]
    context = {'alunos': alunos}
    return render(request, 'aluno_list.html', context)