from django.conf import settings
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


from djshop.auths.users.models import User
from djshop.auths.users.serializers.front import OTPRegisterSerializer, OTPValidateSerializer, \
    OTPRegisterResponseSerializer, OTPValidateResponseSerializer
from djshop.auths.users.utils.otp import OTPService


class AddOTPView(APIView):


    @extend_schema(
        request=OTPRegisterSerializer,
        responses=OTPRegisterResponseSerializer
    )
    def post(self, request: Request):
        serializer = OTPRegisterSerializer(data=request.data)

        if serializer.is_valid():
            user, created= User.objects.get_or_create(phone=serializer.validated_data['phone'])
            OTPService.add_otp(user.phone)
            return Response({"timeout":settings.OTP_TIMEOUT}, status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status.HTTP_400_BAD_REQUEST)


class OTPValidationView(APIView):


    @extend_schema(
        request=OTPValidateSerializer,
        responses=OTPValidateResponseSerializer
    )
    def post(self, request: Request):
        serializer = OTPValidateSerializer(data=request.data)
        if serializer.is_valid():
            is_verify = OTPService.validate_otp(serializer.validated_data["phone"], serializer.validated_data["code"])
            if is_verify:
                token, create = Token.objects.get_or_create(user__phone=serializer.validated_data["phone"])
                token.user.verified_phone = True
                token.user.save(update_fields=["verified_phone"])
                return Response({"token": token.key}, status.HTTP_200_OK)
            else:
                return Response({"errors":"OTP not match"}, status.HTTP_401_UNAUTHORIZED)

        return Response({"errors":serializer.errors}, status.HTTP_400_BAD_REQUEST)
