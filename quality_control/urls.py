from django.urls import path
from . import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),  # Маршрут для получения деталей конкретного бага
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),  # Маршрут для получения деталей конкретного улучшения
]