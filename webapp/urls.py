
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    
    path('', views.index),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
