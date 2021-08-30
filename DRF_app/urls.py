from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'sprints', views.SprintViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'users', views.UserViewSet)
