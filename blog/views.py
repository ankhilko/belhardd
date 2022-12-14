from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_GET

from .models import Post

# Create your views here.

@require_GET
def blog_list(request: HttpRequest):            #функция представления - обрабатывает все запросы
    posts_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts_list})   # не дано передвать папку тэплейт - он автоматом там ищет
    # передаем параметры в документ {'posts': posts_list}, 'a': 'a')   # не дано передвать папку тэплейт - он автоматом там ищет




def post_detail(request: HttpRequest, post_slug: str):
    post = get_object_or_404(Post, slug=post_slug)
    # post = Post.objects.get(slug=post_slug)
    return HttpResponse(f'<br><br>{post.title}<br>')


def error404(request, exception):                       # settings -> defug -> False
    return render(request, 'blog/error_404.html')

