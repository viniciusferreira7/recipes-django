from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from utils.recipe.factory import make_recipe


def home(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name='recipes/pages/home.html',
        context={
            'recipes': [make_recipe() for _ in range(10)]
        }
    )


def recipe(request: HttpRequest, id: int) -> HttpResponse:
    return render(
        request=request,
        template_name='recipes/pages/recipe-view.html',
        context={
            'recipe': make_recipe()
        }
    )
