from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from project.models import Project, Task
from project.serializers import ProjectSerializer, TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ProjectViewSet provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions for project.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, ]


class TaskViewSet(viewsets.ModelViewSet):
    """
    TaskViewSet provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions for Tasks.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, ]


@api_view(['GET'])
def api_root(request, format=None):
    """
    This view provide an api root view.
    """
    return Response({
        'Users': reverse('user-list', request=request, format=format),
        'Projects': reverse('project-list', request=request, format=format),
        'Tasks': reverse('task-list', request=request, format=format),
    })
