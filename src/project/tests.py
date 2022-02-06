from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient

from project.models import Project, Task


class ProjectTests(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        return super().setUp()

    def test_create_project(self):
        """
        Create a project with restAPI
        """
        data = {'name': 'Test Project'}
        response = self.client.post(f'/api/v1/projects/', data, format='json')

        self.assertEqual(response.status_code, 201)
        self.project = response.data
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(self.project['name'], 'Test Project')

    def test_create_task(self):
        """
        Create a teak with restAPI
        """
        self.test_project = Project.objects.create(name='Test')
        data = {'title': 'Test Task', 'status': 'new', 'project': '/api/v1/projects/1/', 'assignee': '/api/v1/users/1/'}
        response = self.client.post(f'/api/v1/tasks/', data, format='json')

        self.assertEqual(response.status_code, 201)
        self.task = response.data
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(self.task['title'], 'Test Task')
        self.assertEqual(self.task['status'], 'new')
        self.assertEqual(self.task['project'], 'http://testserver/api/v1/projects/1/')
        self.assertEqual(self.task['assignee'], 'http://testserver/api/v1/users/1/')
