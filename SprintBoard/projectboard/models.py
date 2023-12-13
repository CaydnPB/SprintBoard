from django.db import models
from django.utils import timezone

class SprintBoardIssue(models.Model):
    all_projects = [
        ('Project 1', 'Project 1'),
        ('Project 2', 'Project 2'),
        ('Project 3', 'Project 3'),
    ]

    all_statuses = [
        ('❌ Not Started ❌', '❌ Not Started ❌'),
        ('⏳ In Progress ⌛️', '⏳ In Progress ⌛️'),
        ('✅ Complete ✅', '✅ Complete ✅'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    project_number = models.ForeignKey('SprintBoardProject', on_delete=models.CASCADE)
    issue_status = models.CharField(max_length=200, choices=all_statuses, default='❌ Not Started ❌')
    creation_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'SprintBoard Issue'
        verbose_name_plural = 'SprintBoard Issues'

class SprintBoardProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    creation_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'SprintBoard Project'
        verbose_name_plural = 'SprintBoad Projects'