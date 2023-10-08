from django.shortcuts import render
from models import Article

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request, 'articles/catch.html', context)

def create_article(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article(title=title, content=content)

    article.save()

    return render(request, 'articles/index.html', context)