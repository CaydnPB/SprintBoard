from django.db import models

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
    project_number = models.CharField(max_length=200, choices=all_projects, default='Project 1')
    issue_status = models.CharField(max_length=200, choices=all_statuses, default='❌ Not Started ❌')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'SprintBoard Issue'
        verbose_name_plural = 'SprintBoard Issues'

class SprintBoardProject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SprintBoard Project'
        verbose_name_plural = 'SprintBoad Projects'