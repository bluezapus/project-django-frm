# Generated by Django 5.1.7 on 2025-03-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_images_alter_category_icons'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug_article',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_category',
            field=models.SlugField(blank=True),
        ),
    ]
