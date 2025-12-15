from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from recipes.models import Recipe


def home(request: HttpRequest) -> HttpResponse:
    recipes = Recipe.objects.all().order_by("-created_at")

    return render(
        request=request,
        template_name='recipes/pages/home.html',
        context={
            'recipes': recipes
        }
    )


def recipe(request: HttpRequest, id: int) -> HttpResponse:
    recipe = Recipe.objects.filter(id=id)

    return render(
        request=request,
        template_name='recipes/pages/recipe-view.html',
        context={
            'recipe': recipe,
            'is_detail_page': True
        }
    )
