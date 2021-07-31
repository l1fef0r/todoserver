
from rest_framework import status, mixins, generics, filters

from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import UserProfile, Todo, Project
from .serializers import UserSerializer, TodoSerializer, ProjectSerializer
from rest_framework.pagination import LimitOffsetPagination

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions


class ProjectPagination(LimitOffsetPagination):
    default_limit = 10

class TodoPagination(LimitOffsetPagination):
    default_limit = 20

class UserView(APIView):

    def get(self, request, format=None):

        users = UserProfile.objects.all()
        serializer = UserSerializer(users, many=True)
        permission_classes = [IsAdminUser]

        return Response(serializer.data)

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()


class UserDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    pagination_class = ProjectPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['$ProjectName']


class ProjectDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class TodoDetail(APIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)



class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    pagination_class = TodoPagination

    filter_backends = [filters.SearchFilter]
    search_fields = ['project']

    def destroy(self, request, pk):
        tod = self.queryset.get(pk=int(pk))
        data = TodoSerializer(tod).data
        data['open'] = False
        return Response(data)

