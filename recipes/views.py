from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Home page")


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Contact page")


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("About page")
