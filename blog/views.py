from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from . models import Article, Category, Comment
from . forms import CommentsForm
from taggit.models import Tag

def index(request, slug_input=None):
    list_article = Article.objects.all().order_by('-publish') #take all list from model
    list_category = Category.objects.all()
    recent_article = Article.objects.all().order_by('-publish')[:3]
    list_tag = Tag.objects.all()

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
        'tags': list_tag,
    }
    return render(request, 'blog/index.html', context)

def tagged(request, tags_input):
    tags = Tag.objects.get(slug=tags_input)
    common_tags = Article.tags.most_common()[:10]
    article_tags = Article.objects.filter(tags=tags)
    list_categories = Category.objects.all()

    context = {
        'title': 'Article Tags',
        'article_tags': article_tags,
        'common_tags': common_tags,
        'list_categories': list_categories,
    }
    return render(request, 'blog/article_tags.html', context)

def detail(request, slug_input):
    detail_article = Article.objects.get(slug_article=slug_input) #for comment too
    others_article = Article.objects.exclude(slug_article=slug_input).order_by('-publish')[:3] #not same article recent
    list_category = Category.objects.all()
    # tags
    list_tag = Tag.objects.all()
    # var view coment
    comment_article = Comment.objects.filter(articles=detail_article, reply=None).order_by('-timestamp')

    # add comment script
    if request.method == 'POST':
        form = CommentsForm(request.POST or None)
        if form.is_valid():
            comment = request.POST.get('comments')
            reply = request.POST.get('comment_slug')
            comments = None
            if reply:
                comments = Comment.objects.get(id=reply)
            comment = Comment.objects.create(
                articles=detail_article, 
                user=request.user, 
                comments=comment, 
                reply=comments
            )
            form = CommentsForm()
            return redirect('blog:detail', slug_input=slug_input)
    else:
        form = CommentsForm()

    context = {
        'title': 'Detail Blog',
        'detail_article': detail_article,
        'others_article': others_article,
        'categories': list_category,
        #var obj coment
        'form': form,
        'comments': comment_article, 
        # tag
        'tags': list_tag,
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
