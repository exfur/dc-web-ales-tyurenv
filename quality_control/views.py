from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.views import View

from django.views.generic import DetailView

from .models import BugReport, FeatureRequest
from .forms import BugReportForm, FeatureRequestForm

def index(request):
    return render(request, 'quality_control/index.html')


def bug_list(request):
    bug_reports = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_reports': bug_reports})


def bug_detail(request, bug_id):
    bug_report = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug_report': bug_report})


def bug_create(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})


def bug_update(request, bug_id):
    bug_report = get_object_or_404(BugReport, id=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug_report)
        if form.is_valid():
            form.save()
            return redirect('bug_detail', bug_id=bug_report.id)
    else:
        form = BugReportForm(instance=bug_report)
    return render(request, 'quality_control/bug_report_form.html', {'form': form})


def bug_delete(request, bug_id):
    bug_report = get_object_or_404(BugReport, id=bug_id)
    if request.method == 'POST':
        bug_report.delete()
        return redirect('bug_list')
    return render(request, 'quality_control/bug_confirm_delete.html', {'bug_report': bug_report})


def feature_list(request):
    feature_requests = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_requests': feature_requests})


def feature_detail(request, feature_id):
    feature_request = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature_request': feature_request})


def feature_create(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feature_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

# Update view for FeatureRequest
def feature_update(request, feature_id):
    feature_request = get_object_or_404(FeatureRequest, id=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature_request)
        if form.is_valid():
            form.save()
            return redirect('feature_detail', feature_id=feature_request.id)
    else:
        form = FeatureRequestForm(instance=feature_request)
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

# Delete view for FeatureRequest
def feature_delete(request, feature_id):
    feature_request = get_object_or_404(FeatureRequest, id=feature_id)
    if request.method == 'POST':
        feature_request.delete()
        return redirect('feature_list')
    return render(request, 'quality_control/feature_confirm_delete.html', {'feature_request': feature_request})
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


def add_bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug_list')  # Redirect to bug list page after successful submission
    else:
        form = BugReportForm()
    return render(request, 'bug_report_form.html', {'form': form})