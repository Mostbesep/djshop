from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken

from djshop.auths.users.models import User
from djshop.auths.users.serializers.admin import AdminLoginSerializer, UserManagementSerializer


class AdminLoginView(ObtainAuthToken):
    serializer_class = AdminLoginSerializer


class UserManagementViewSet (viewsets.ModelViewSet):
    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserManagementSerializer