from django.db import models
from django.contrib.auth.models import AbstractUser



class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    password = models.CharField(default='123', max_length=128)
    username = models.CharField(default='name', max_length=128, unique=True)

    def __str__(self):
        return self.username


class Project(models.Model):
    ProjectName = models.CharField(max_length=128, blank=True)
    url = models.URLField(max_length=128)
    user = models.ManyToManyField(UserProfile)

    def __str__(self):
        return self.ProjectName

class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    open = models.BooleanField(blank=True)
    text = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

