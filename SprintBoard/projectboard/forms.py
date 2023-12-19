# forms.py
from django import forms
from .models import SprintBoardIssue, SprintBoardProject

class SprintBoardIssueForm(forms.ModelForm):
    class Meta:
        model = SprintBoardIssue
        fields = ['title', 'description', 'project_number', 'issue_status']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['project_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['issue_status'].widget.attrs.update({'class': 'form-control'})

class SprintBoardProjectForm(forms.ModelForm):
    class Meta:
        model = SprintBoardProject
        fields = ['title', 'description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})