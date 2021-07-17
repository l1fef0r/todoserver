from rest_framework.viewsets import ModelViewSet

from .models import UserProfile
from .serializers import UserSerializer

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()