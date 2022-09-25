from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class NewsAdmin (admin.ModelAdmin):
    list_display = ('id','title', 'created_at', 'updated_at','is_published','categories', 'views', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'categories')
    fields = ('title','categories', 'content', 'created_at', 'updated_at','is_published', 'views', 'photo', 'get_photo')
    readonly_fields = ('created_at', 'updated_at','get_photo')
    save_on_top = True
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'
    get_photo.short_description = 'Миниатюра'


class CategoryAdmin (admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.site_title = 'Аминистрирование новостей'
admin.site.site_header = 'Аминистрирование новостей'