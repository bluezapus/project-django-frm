from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    slug_category = models.SlugField(blank=True)
    icons = models.ImageField(blank=True, default='category.png', upload_to='categoty/')

    def save(self, *args, **kwargs):
        self.slug_article = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Article(models.Model):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE) #relation database
    title = models.CharField(max_length=250)
    fill = models.TextField()
    images = models.ImageField(
        blank=True, default='article.png', upload_to='articles/')
    slug_article = models.SlugField(blank=True, editable=False)
    # tags
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug_article = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
