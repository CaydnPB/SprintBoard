# Generated by Django 4.2.8 on 2023-12-13 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projectboard', '0004_sprintboardproject_pub_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sprintboardproject',
            old_name='pub_date',
            new_name='creation_time',
        ),
        migrations.RemoveField(
            model_name='sprintboardissue',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='sprintboardissue',
            name='creation_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]