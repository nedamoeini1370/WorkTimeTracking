from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from account.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A view set for viewing, creating and viewing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
