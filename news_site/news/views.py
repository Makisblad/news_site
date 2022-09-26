from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages



class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 2
    #extra_context = {'title':'Список новостей'}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('categories')# для жадной загрузки и скоращения sql-запросов

class NewsByCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False # запрет показа пустых списков
    paginate_by = 2

    def get_queryset(self):
        return News.objects.filter(categories_id=self.kwargs['categories_id']).select_related('categories')# для жадной загрузки и скоращения sql-запросов

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['categories_id'])
        return context


# def index(request):
#     news = News.objects.order_by('-created_at')
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'news/index.html', context)
#
# def get_category(request, categories_id):
#     news = News.objects.filter(categories_id=categories_id)
#     category = Category.objects.get(pk=categories_id)
#     return render(request, 'news/category.html', {'news': news, 'category': category})
#
# def view_news(request,news_id):
#     #news = News.objects.(pk=news_id)
#     news =get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {'news': news})

class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'news'

class AddNews(LoginRequiredMixin,CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, "news/register.html", {'form': form})


def login(request):
    return render(request, "news/login.html")


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             #news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
#
#
