from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from users.views import ProjectViewSet, TodoViewSet, UserView, UserDetail, ProjectDetail, TodoDetail


router = SimpleRouter()

router.register('projects', ProjectViewSet)
router.register('todos', TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/users/', UserView.as_view()),
    path('api/users/<int:pk>/', UserDetail.as_view()),
    path('api/projects/<int:pk>', ProjectDetail.as_view()),
    path('api/todos/<int:pk>', TodoDetail.as_view()),
]
