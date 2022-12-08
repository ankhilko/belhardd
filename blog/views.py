from django.shortcuts import render, HttpResponse
from django.http import HttpRequest

# Create your views here.


def blog_list(request: HttpRequest):            #функция представления - обрабатывает все запросы
    return HttpResponse('<b>Hello</b>')


