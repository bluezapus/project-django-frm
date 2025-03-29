from django.shortcuts import render

from . models import Article, Category

def index(request):
    list_article = Article.objects.all().order_by('-publish') #take all list from model
    context = {
        'title': 'Blog',
        'articles': list_article,
    }
    return render(request, 'blog/index.html', context)

def detail(request, slug_input):
    detail_article = Article.objects.get(slug_article=slug_input)
    context = {
        'title': 'Detail Blog',
        'detail_article': detail_article,
    }

    return render(request, 'blog/detail.html', context)
