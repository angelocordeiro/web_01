from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('aluno_list/<int:id>', views.aluno_list,name="aluno_list"),
    path('contato/', views.contato, name='contato'),
]