from django.shortcuts import render
from django.http import HttpResponse
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


