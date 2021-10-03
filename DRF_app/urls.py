from . import views
from rest_framework.routers import DefaultRouter


app_name = 'DRF_app'

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'post_comments', views.PostCommentViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'sessions', views.SessionViewSet)
