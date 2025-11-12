from django.urls import path

from typing import List, Union
from django.urls.resolvers import URLPattern, URLResolver
from recipes.views import home, contact, about

urlpatterns: List[Union[URLPattern, URLResolver]] = [
    path('', home),
    path('contact/', contact),
    path('about/', about)
]
