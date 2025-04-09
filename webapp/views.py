from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Creative & Innovative Digital Solution',
        'nav': [
            ['/','home'],
            ['/blog','blog'],
            ['/contact','contact'],
        ]
    }
    return render(request, 'index.html', context)

def heandler404(request):
    context = {
        'title': 'Page Not Found'
    }
    return render(request, '404.html', context, status=404)