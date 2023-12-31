# Generated by Django 4.2.8 on 2023-12-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SprintBoardIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('project_number', models.CharField(choices=[('Project 1', 'Project 1'), ('Project 2', 'Project 2'), ('Project 3', 'Project 3')], default='Project 1', max_length=200)),
                ('issue_status', models.CharField(choices=[('❌ Not Started ❌', '❌ Not Started ❌'), ('⏳ In Progress ⌛️', '⏳ In Progress ⌛️'), ('✅ Complete ✅', '✅ Complete ✅')], default='❌ Not Started ❌', max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'verbose_name': 'SprintBoard Issue',
                'verbose_name_plural': 'SprintBoard Issues',
            },
        ),
    ]
