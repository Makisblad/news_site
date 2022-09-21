from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeNews.as_view(), name='home'),
    path("category/<int:categories_id>/", NewsByCategory.as_view(), name='category'),
    path("news/<int:pk>", ViewNews.as_view(), name='view_news'),
    path("news/add_news/", AddNews.as_view(), name='add_news')

]