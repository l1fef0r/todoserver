from django.contrib import admin
from .models import UserProfile, Todo, Project
from django.contrib import admin

admin.site.register(UserProfile)
admin.site.register(Todo)
admin.site.register(Project)

