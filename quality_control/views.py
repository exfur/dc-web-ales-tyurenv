from django.shortcuts import HttpResponse
from django.urls import reverse
from django.http import HttpResponse

def index(request):
    quality_control_url = reverse('quality_control:index')
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')

    html = f"<h1>Система контроля качества</h1>"
    html += f"<p><a href='{quality_control_url}'>Главная страница</a></p>"
    html += f"<p><a href='{bug_list_url}'>Список отчетов об ошибках</a></p>"
    html += f"<p><a href='{feature_list_url}'>Список запросов на улучшение</a></p>"
    
    return HttpResponse(html)

def bug_list(request):
    return HttpResponse("<h1>Список отчетов об ошибках</h1>")

def feature_list(request):
    return HttpResponse("<h1>Список запросов на улучшение</h1>")

def bug_detail(request, bug_id):
    return HttpResponse(f"<h1>Детали бага {bug_id}</h1>")

def feature_detail(request, feature_id):
    return HttpResponse(f"<h1>Детали улучшения {feature_id}</h1>")
