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