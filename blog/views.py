from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    all_articles = Article.objects.all()

    context = {
            "all_articles" : all_articles}
    return render(request, 'blog_index.html', context)


