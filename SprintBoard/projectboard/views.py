from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import SprintBoardIssue, SprintBoardProject
from .forms import SprintBoardIssueForm, SprintBoardProjectForm

def home(request):
    issues = SprintBoardIssue.objects.all()
    projects = SprintBoardProject.objects.all()
    return render(request, "projectboard/home.html", {'issues': issues, 'projects': projects})

def account(request):
    return render(request, 'projectboard/account.html')

def projects(request):
    return render(request, 'projectboard/projects.html')

def create(request):
    return render(request, 'projectboard/createproject.html')

def createproject(request, projectname):
    context = {
        'projectname': projectname,
    }
    return render(request, 'projectboard/createproject.html', context)

def createissue(request):
    if request.method == 'POST':
        form = SprintBoardIssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SprintBoardIssueForm()
    return render(request, 'projectboard/createissue.html', {'form': form})

def updateissue(request, issue_id):
    issue = get_object_or_404(SprintBoardIssue, pk=issue_id)
    if request.method == 'POST':
        form = SprintBoardIssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SprintBoardIssueForm(instance=issue)
    return render(request, 'projectboard/updateissue.html', {'form': form, 'issue': issue})

def deleteissue(request, issue_id):
    issue = get_object_or_404(SprintBoardIssue, pk=issue_id)
    if request.method == 'POST':
        issue.delete()
        return redirect('/')
    return render(request, 'projectboard/deleteissue.html', {'issue': issue})