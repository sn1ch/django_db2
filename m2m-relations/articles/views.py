from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Tag, ArticleTag


def articles_list(request):
    template = 'articles/news.html'
    news = []

    articles = Article.objects.all()
    article_tag = Article.objects.all().prefetch_related('tag', 'articletag'). \
        values_list('id', 'articletag__is_main', 'tag__tag')

    for i in articles:
        item = {
            'title': i.title,
            'text': i.text,
            'published_at': i.published_at,
            'image': i.image,
            'scopes': {'all': []}
        }
        for id in article_tag:
            if i.id == id[0] and id[2] is not None:
                scopes = {
                    'is_main': id[1],
                    'topic': id[2]
                }
                item['scopes']['all'].append(scopes)
            else:
                continue
        news.append(item)
        print(item)

    context = {'object_list': news}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
