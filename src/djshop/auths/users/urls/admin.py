from django.urls import path
from rest_framework.routers import SimpleRouter

from djshop.auths.users.views.admin import AdminLoginView, UserManagementViewSet

router = SimpleRouter()
router.register('users',UserManagementViewSet , basename='User Management')
urlpatterns = [
                  path('login/', AdminLoginView.as_view()),
              ] + router.urls