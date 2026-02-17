from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Post


def home_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='index.html')


def about_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='about.html')


def posts_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='posts.html', context={'posts': Post.objects.all()})

