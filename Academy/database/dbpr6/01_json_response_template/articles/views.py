from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

def article_html(request): # HTML 응답
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/article.html', context)


def article_json_1(request): # JsonResponse() 이용 JSON 응답
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
            'id': article.pk,
            'title': article.title,
            'content': article.content,
            'created_at': article.created_at,
            'updated_at': article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False)


def article_json_2(request): # Django Serializer 이용 JSON 응답
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')

@api_view(['GET'])
def article_json_3(request): # Django REST framework 이용 JSON 응답
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    # many=True : 객체가 하나가 아닐 때 사용
    return Response(serializer.data)
