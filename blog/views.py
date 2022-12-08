from django.shortcuts import render, HttpResponse
from django.http import HttpRequest
from .models import Post

# Create your views here.


def blog_list(request: HttpRequest):            #функция представления - обрабатывает все запросы
    return HttpResponse('<b>Hello</b>')



def post_detail(request: HttpRequest, post_slug: str):
    post = Post.objects.get(slug=post_slug)
    return HttpResponse(f'<br><br>{post.title}<br>')
