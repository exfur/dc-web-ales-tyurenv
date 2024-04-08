from django.urls import path, reverse
from django.http import HttpResponse

def index(request):
    quality_control_url = reverse('quality_control:index')  # Получаем URL главной страницы приложения quality_control
    return HttpResponse(f"<h1>Страница приложения tasks</h1><a href='{quality_control_url}'>Перейти на главную страницу приложения quality_control</a>")

def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")