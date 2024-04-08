from django.urls import path
from . import views
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    #path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    #path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),  # Маршрут для получения деталей конкретного бага
    #path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),  # Маршрут для получения деталей конкретного улучшения

    path('', views.IndexView.as_view(), name='index'),
    path('bugs/<int:bug_id>/', views.BugReportDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureRequestDetailView.as_view(), name='feature_request_detail'),
]