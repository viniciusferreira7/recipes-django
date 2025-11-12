from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='recipes/home.html', context={
        "name": "John Doe"
    })


def contact(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='home.html')


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("About page")
