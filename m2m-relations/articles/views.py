from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    a = Article.objects.all()
    news = []
    print(a)
    for i in Article.objects.all():
        item = {
            'title': i.title,
            'text': i.text,
            'published_at': i.published_at,
            'image': i.image
        }
        news.append(item)
    context = {'object_list': news}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
