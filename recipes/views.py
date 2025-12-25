from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from recipes.models import Recipe, Category
from uuid import UUID


def home(request: HttpRequest) -> HttpResponse:
    recipes = Recipe.objects.filter(is_published=True).order_by("-created_at")

    return render(
        request=request,
        template_name='recipes/pages/home.html',
        context={
            'title': "Home | Recipes",
            'recipes': recipes
        }
    )


def recipe(request: HttpRequest, id: UUID) -> HttpResponse:
    recipe = get_object_or_404(Recipe, id=id, is_published=True)

    return render(
        request=request,
        template_name='recipes/pages/recipe-view.html',
        context={
            'title': f"{recipe.title} | Recipes",
            'recipe': recipe,
            'is_detail_page': True
        }
    )


def category(request: HttpRequest, category_id: UUID) -> HttpResponse:
    category = get_object_or_404(Category, id=category_id)
    recipes = Recipe.objects.filter(
        category=category,
        is_published=True).order_by("-created_at")

    return render(
        request=request,
        template_name='recipes/pages/category.html',
        context={
            'title': f"{category.name} | Categories",
            'category': category,
            'recipes': recipes,
        }
    )
