from django.urls import path
from rest_framework.routers import SimpleRouter

from djshop.auths.users.views.front import AddOTPView, OTPValidationView

router = SimpleRouter()

urlpatterns = [
        path('otp/register', AddOTPView.as_view()),
        path('otp/verify', OTPValidationView.as_view()),
              ] + router.urls