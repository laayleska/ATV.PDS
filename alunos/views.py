from django.shortcuts import render

# Create your views here.

def lista(request):
    return render(request, 'lista.html')

def novo(request):
    return render(request, 'novo.html')

def detalhe(request):
    return render(request, 'detalhe.html')