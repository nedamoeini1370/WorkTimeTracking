from django.urls import path
from rest_framework.routers import SimpleRouter

from project.views import ProjectViewSet, TaskViewSet, api_root

router = SimpleRouter()
router.register('projects', ProjectViewSet, basename='project')
router.register('tasks', TaskViewSet, basename='task')

urlpatterns = router.urls

urlpatterns += [
    path('', api_root),
]
