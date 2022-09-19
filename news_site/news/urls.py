from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='home'),
    path("category/<int:categories_id>/", get_category, name='category')

]