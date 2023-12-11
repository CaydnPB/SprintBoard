from django.http import HttpResponse
from django.shortcuts import render
from .models import ProjectBoardIssue

def projectboard(request):
    issues = ProjectBoardIssue.objects.all()
    return render(request, "projectboard/body.html", {'issues': issues})

def projectdetail(request):
    return render(request, 'projectboard/projectdetail.html')

def projectcreate(request, projectname):
    context = {
        'projectname': projectname,
    }
    return render(request, 'projectboard/projectcreate.html', context)