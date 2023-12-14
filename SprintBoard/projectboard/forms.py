# forms.py
from django import forms
from .models import SprintBoardIssue, SprintBoardProject

class SprintBoardIssueForm(forms.ModelForm):
    class Meta:
        model = SprintBoardIssue
        fields = ['title', 'description', 'project_number', 'issue_status']

class SprintBoardProjectForm(forms.ModelForm):
    class Meta:
        model = SprintBoardProject
        fields = ['title', 'description']