from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *

def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context)

def get_category(request, categories_id):
    news = News.objects.filter(categories_id=categories_id)
    category = Category.objects.get(pk=categories_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})

def view_news(request,news_id):
    #news = News.objects.(pk=news_id)
    news =get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news': news})


