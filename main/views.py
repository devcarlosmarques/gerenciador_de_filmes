from django.shortcuts import render
from .models import Filme

def filmes(request):
    lista_filmes = Filme.objects.all()
    return render(request,'filmes.html', {'lista_filmes':lista_filmes})
