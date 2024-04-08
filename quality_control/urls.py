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
    path('bugs/create/', views.bug_create, name='bug_create'),
    path('features/<int:feature_id>/', views.FeatureRequestDetailView.as_view(), name='feature_request_detail'),
    path('bugs/<int:bug_id>/update/', views.bug_update, name='update_bug'),
    path('bugs/<int:bug_id>/delete/', views.bug_update, name='delete_bug_confirm'),
    path('features/<int:feature_id>/update/', views.feature_update, name='update_feature'),
    path('features/<int:feature_id>/delete/', views.feature_delete, name='delete_feature_confirm'),
    path('feature_request_form/', views.feature_create, name='feature_create'),
] 