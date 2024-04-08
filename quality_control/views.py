from django.shortcuts import HttpResponse
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from .models import BugReport, FeatureRequest

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
    bug_reports = BugReport.objects.all()
    response_data = "<h1>Bug Report List</h1>"
    for bug_report in bug_reports:
        response_data += f"<p><strong>{bug_report.title}</strong> - {bug_report.status} "
        response_data += f"(<a href='/bug-report/{bug_report.id}/'>Details</a>)</p>"
    return HttpResponse(response_data)

def feature_list(request):
    feature_requests = FeatureRequest.objects.all()
    response_data = "<h1>Feature Request List</h1>"
    for feature_request in feature_requests:
        response_data += f"<p><strong>{feature_request.title}</strong> - {feature_request.status} "
        response_data += f"(<a href='/feature-request/{feature_request.id}/'>Details</a>)</p>"
    return HttpResponse(response_data)


def bug_detail(request, bug_id):
    return HttpResponse(f"<h1>Детали бага {bug_id}</h1>")

def feature_detail(request, feature_id):
    return HttpResponse(f"<h1>Детали улучшения {feature_id}</h1>")


class IndexView(View):
    def get(self, request):
        return HttpResponse("<h1>Главная страница приложения Quality Control (CBV)</h1>")

class BugReportDetailView(View):
    def get(self, request, bug_id):
        try:
            bug_report = BugReport.objects.get(id=bug_id)
            response_data = f"<h1>{bug_report.title}</h1>"
            response_data += f"<p><strong>Description:</strong> {bug_report.description}</p>"
            response_data += f"<p><strong>Status:</strong> {bug_report.status}</p>"
            response_data += f"<p><strong>Priority:</strong> {bug_report.priority}</p>"
            response_data += f"<p><strong>Project:</strong> {bug_report.project}</p>"
            response_data += f"<p><strong>Task:</strong> {bug_report.task}</p>"
            return HttpResponse(response_data)
        except BugReport.DoesNotExist:
            return HttpResponse("<h1>Bug Report not found</h1>", status=404)

class FeatureRequestDetailView(View):
    def get(self, request, feature_id):
        try:
            feature_request = FeatureRequest.objects.get(id=feature_id)
            response_data = f"<h1>{feature_request.title}</h1>"
            response_data += f"<p><strong>Description:</strong> {feature_request.description}</p>"
            response_data += f"<p><strong>Status:</strong> {feature_request.status}</p>"
            response_data += f"<p><strong>Priority:</strong> {feature_request.priority}</p>"
            response_data += f"<p><strong>Project:</strong> {feature_request.project}</p>"
            response_data += f"<p><strong>Task:</strong> {feature_request.task}</p>"
            return HttpResponse(response_data)
        except FeatureRequest.DoesNotExist:
            return HttpResponse("<h1>Feature Request not found</h1>", status=404)