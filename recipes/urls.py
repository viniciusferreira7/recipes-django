from django.urls import path

from typing import List, Union
from django.urls.resolvers import URLPattern, URLResolver
from recipes import views

app_name = "recipes"

urlpatterns: List[Union[URLPattern, URLResolver]] = [
    path('', views.home, name="home"),
    path('recipes/<uuid:id>/', views.recipe, name="recipe"),
    path(
        'recipes/category/<uuid:category_id>/',
        views.category,
        name="category")
]
