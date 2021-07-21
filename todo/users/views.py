from rest_framework.viewsets import ModelViewSet

from .models import UserProfile, Todo, Project
from .serializers import UserSerializer, TodoSerializer, ProjectSerializer

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

