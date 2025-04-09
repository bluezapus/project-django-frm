from django.db import models
from django.utils.text import slugify
from django.conf import settings
from taggit.managers import TaggableManager


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    slug_category = models.SlugField(blank=True, editable=False)
    icons = models.ImageField(blank=True, default='category.png', upload_to='categoty/')

    def save(self, *args, **kwargs):
        self.slug_category = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)
    # def save(self, *args, **kwargs):
    #     self.slug_category = slugify(self.title, allow_unicode=True).replace(' ', '-')
    #     return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Article(models.Model):
    users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) #relation database
    title = models.CharField(max_length=250)
    fill = models.TextField()
    images = models.ImageField(
        blank=True, default='article.png', upload_to='articles/')
    slug_article = models.SlugField(blank=True, editable=False)
    tags = TaggableManager()
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug_article = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

# Commeent
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)
    articles = models.ForeignKey(Article, on_delete=models.CASCADE)
    comments = models.TextField()
    reply = models.ForeignKey('self', null=True, blank=True, related_name='replies', max_length=250, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.articles.title} - {self.comments} {self.user.name}"