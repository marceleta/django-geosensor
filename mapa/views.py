from django.shortcuts import render
from django.http import HttpResponse


def helloworld(request):
    return render(request, 'mapa/helloworld.html')