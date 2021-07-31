from rest_framework.serializers import ModelSerializer


from .models import UserProfile, Project, Todo

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


