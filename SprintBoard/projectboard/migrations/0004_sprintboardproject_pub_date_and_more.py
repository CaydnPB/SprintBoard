# Generated by Django 4.2.8 on 2023-12-13 15:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projectboard', '0003_sprintboardproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprintboardproject',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='sprintboardissue',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Creation Time'),
        ),
    ]
