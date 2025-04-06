from django.shortcuts import render
from django.core.paginator import Paginator

from . models import Article, Category

def index(request, slug_input=None):
    list_article = Article.objects.all().order_by('-publish') #take all list from model
    list_category = Category.objects.all()
    recent_article = Article.objects.all().order_by('-publish')[:3]

    #paginations
    paginator = Paginator(Article.objects.all(), 8)
    page_number = request.GET.get("page")
    articles = paginator.get_page(page_number)

    context = {
        'title': 'Blog',
        'list_articles': list_article,
        'categories': list_category,
        'recent_article': recent_article,
        'articles': articles,
    }
    return render(request, 'blog/index.html', context)

def detail(request, slug_input):
    detail_article = Article.objects.get(slug_article=slug_input)
    others_article = Article.objects.exclude(slug_article=slug_input).order_by('-publish')[:3] #not same article recent
    list_category = Category.objects.all()
    context = {
        'title': 'Detail Blog',
        'detail_article': detail_article,
        'others_article': others_article,
        'categories': list_category,
    }

    return render(request, 'blog/detail.html', context)

def category(request, category_input):
    Category_articles = Article.objects.filter(categories__title=category_input) #take category with relation database (title from article)
    category_choices = Category.objects.order_by('id') #with id from category, if use publish (create first publish on models category)
    recent_article = Article.objects.all().order_by('-publish')[:3]
    context = {
        'title': 'Category',
        'category_articles': Category_articles,
        'category_choices': category_choices,
        'recent_article': recent_article,
    }
    return render(request, 'blog/category.html', context)
