from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

TASK_STATUSES = (
    ('new', 'New'),
    ('in_progress', 'In Progress'),
    ('suspend', 'Suspend'),
    ('done', 'Done'),
)


class Project(models.Model):
    """
    Project in a task manager system are represented by this
    model.

    name is required. Other fields are optional.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    assigned_to = models.ManyToManyField(
        User, blank=True, related_name="assignees")

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    This model represents tasks of projects.
    """
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=TASK_STATUSES, default=TASK_STATUSES[0])
    project = models.ForeignKey(Project, related_name='project', on_delete=models.PROTECT)
    assignee = models.ForeignKey(User, related_name="assignee", on_delete=models.PROTECT)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    suspend_date = models.DateTimeField(blank=True, null=True)
    total_suspend_time = models.PositiveBigIntegerField(blank=True, null=True, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['title', 'project']

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        self.old_status = self.status

    def get_total_time_second(self) -> int:
        """
        Calculate total time is spent on the task in second.
        """
        start_date = self.start_date
        end_date = self.end_date
        if self.status == 'new':
            return 0
        if not end_date:
            if self.status == 'suspend':
                end_date = self.suspend_date
            else:
                end_date = timezone.now()
        delta = end_date - start_date

        return delta.total_seconds() - self.total_suspend_time

    @property
    def total_time(self) -> str:
        """
        Calculate total time is spent on the task in day:hours:min:sec format.
        """
        sec = timedelta(0, self.get_total_time_second())
        return "%s" % str(sec).split('.')[0]

    def save(self, *args, **kwargs):
        if self.status:
            current_tz = timezone.get_current_timezone()
            if self.old_status == 'new' and self.status == 'in_progress':
                self.start_date = datetime.now(current_tz)
            elif self.old_status == 'in_progress' and self.status == 'done':
                self.end_date = datetime.now(current_tz)
            elif self.old_status == 'in_progress' and self.status == 'suspend':
                self.suspend_date = datetime.now(current_tz)
            elif self.old_status == 'suspend' and self.status == 'in_progress':
                delta = (datetime.now(current_tz) - self.suspend_date).total_seconds()
                self.total_suspend_time = self.total_suspend_time + delta

        return super(Task, self).save(*args, **kwargs)
