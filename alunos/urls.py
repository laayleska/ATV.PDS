
app_name = 'alunos'

from django.contrib import admin
from django.urls import path
from .views import lista, novo, detalhe

urlpatterns = [
    path('lista/', lista, name='lista.html'),
    path('novo/', novo, name='novo.html'),
    path('detalhe/', detalhe, name='detalhe.html'),
]



