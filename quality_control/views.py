from django.shortcuts import HttpResponse, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from django.views.generic import DetailView

from .models import BugReport, FeatureRequest

def index(request):
    return render(request, 'quality_control/index.html')

def bug_list(request):
    bug_reports = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_reports': bug_reports})

def feature_list(request):
    feature_requests = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_requests': feature_requests})

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})


class IndexView(View):
    def get(self, request):
        return render(request, 'quality_control/index.html')

class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'

class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'