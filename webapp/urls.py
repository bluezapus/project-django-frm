
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings #import media images

from . import views
from django.conf.urls.static import static # import static

urlpatterns = [
    
    path('', views.index, name='index'),
    path('about/', include('about.urls', namespace='about')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('accounts/', include('account.urls', namespace='account')), #logout
    path('accounts/', include('django.contrib.auth.urls')), #login
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # add MEDIA for urls

heandler404 = "webapp.views.handler404"
