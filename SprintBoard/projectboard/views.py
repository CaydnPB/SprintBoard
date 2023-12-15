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

def createproject(request):
    if request.method == 'POST':
        form = SprintBoardProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SprintBoardProjectForm()
    return render(request, 'projectboard/createproject.html', {'form': form})

def updateproject(request, project_id):
    project = get_object_or_404(SprintBoardProject, pk=project_id)
    if request.method == 'POST':
        form = SprintBoardProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SprintBoardProjectForm(instance=project)
    return render(request, 'projectboard/updateproject.html', {'form': form, 'project': project})

def deleteproject(request, project_id):
    project = get_object_or_404(SprintBoardProject, pk=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('/')
    return render(request, 'projectboard/deleteproject.html', {'project': project})

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

def projects(request):
    projects = SprintBoardProject.objects.all()
    return render(request, 'projectboard/projects.html', {'projects': projects})

def projectsdetail(request, project_id):
    project = get_object_or_404(SprintBoardProject, pk=project_id)
    issues_by_status = {
        'not_started': SprintBoardIssue.objects.filter(project_number=project, issue_status='❌ Not Started ❌'),
        'in_progress': SprintBoardIssue.objects.filter(project_number=project, issue_status='⏳ In Progress ⌛️'),
        'complete': SprintBoardIssue.objects.filter(project_number=project, issue_status='✅ Complete ✅'),
    }
    return render(request, 'projectboard/projectsdetail.html', {'project': project, 'issues_by_status': issues_by_status})