from django.contrib import admin
from .models import SprintBoardIssue, SprintBoardProject

admin.site.register(SprintBoardIssue)
admin.site.register(SprintBoardProject)