from django.http import HttpResponse
from django.shortcuts import render
from .models import ProjectBoardIssue

def home(request):
    issues = ProjectBoardIssue.objects.all()
    return render(request, "projectboard/home.html", {'issues': issues})

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