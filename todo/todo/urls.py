from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from users.views import ProjectViewSet, TodoViewSet, UserView, UserDetail, ProjectDetail, TodoDetail, UserViewSet


router = DefaultRouter()
router.register('all_users', UserViewSet, basename='all_users')
router.register('projects', ProjectViewSet)
router.register('todos', TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls)),
    path('api/users/', UserView.as_view()),
    path('api/users/<int:pk>/', UserDetail.as_view()),
    path('api/projects/<int:pk>', ProjectDetail.as_view()),
    path('api/todos/<int:pk>', TodoDetail.as_view()),
    path('api/todos/<int:pk>', TodoViewSet.as_view({'get': 'list'})),
]
