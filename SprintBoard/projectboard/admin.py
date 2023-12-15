from django.contrib import admin
from .models import SprintBoardIssue, SprintBoardProject
from django import forms

class SprintBoardIssueForm(forms.ModelForm):
    class Meta:
        model = SprintBoardIssue
        fields = '__all__'

class SprintBoardIssueAdmin(admin.ModelAdmin):
    form = SprintBoardIssueForm

class SprintBoardProjectForm(forms.ModelForm):
    class Meta:
        model = SprintBoardProject
        fields = '__all__'

class SprintBoardProjectAdmin(admin.ModelAdmin):
    form = SprintBoardProjectForm

admin.site.register(SprintBoardIssue, SprintBoardIssueAdmin)
admin.site.register(SprintBoardProject)
