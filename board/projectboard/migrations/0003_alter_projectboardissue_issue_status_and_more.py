# Generated by Django 4.2.8 on 2023-12-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectboard', '0002_alter_projectboardissue_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectboardissue',
            name='issue_status',
            field=models.IntegerField(choices=[('❌ Not Started ❌', '❌ Not Started ❌'), ('⏳ In Progress ⌛️', '⏳ In Progress ⌛️'), ('✅ Complete ✅', '✅ Complete ✅')], default='❌ Not Started ❌'),
        ),
        migrations.AlterField(
            model_name='projectboardissue',
            name='project_number',
            field=models.IntegerField(choices=[('Project 1', 'Project 1'), ('Project 2', 'Project 2'), ('Project 3', 'Project 3')], default='Project 1'),
        ),
    ]
