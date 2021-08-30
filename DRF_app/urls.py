from django.contrib import admin
from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'sprints', views.SprintViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'users', views.UserViewSet)

# urlpatterns = [
#     path('', views.index, name='drf_index_page'),
#     path('pr1', views.pr1, name='drf_pr1'),
# ]
