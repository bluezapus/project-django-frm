# Generated by Django 5.1.7 on 2025-03-29 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_slug_article_slug_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug_article',
            field=models.SlugField(blank=True, editable=False),
        ),
    ]
