# Generated by Django 4.0.1 on 2022-02-06 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_project_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('title', 'project')},
        ),
    ]
