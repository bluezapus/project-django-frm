from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('tags/<slug:tags_input>/', views.tagged, name='blog_tags'),
    path('category/<slug:category_input>/', views.category, name='blog_category'),
    path('detail/<slug:slug_input>/', views.detail, name='blog_detail'),
    path('', views.index, name='blog_index'),
]