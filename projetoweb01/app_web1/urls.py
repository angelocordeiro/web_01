from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('aluno_list', views.aluno_list,name="aluno_list"),
    path('aluno2', views.aluno2,name="aluno2"),
]