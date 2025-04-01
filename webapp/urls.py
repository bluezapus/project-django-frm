
from django.contrib import admin
from django.urls import path, include
from django.conf import settings #import media images

from . import views
from django.conf.urls.static import static # import static

urlpatterns = [
    
    path('', views.index),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('account.urls', namespace='account')), #logout
    path('accounts/', include('django.contrib.auth.urls')), #login
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # add MEDIA for urls
