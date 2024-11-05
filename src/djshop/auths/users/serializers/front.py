import re

from rest_framework import serializers


class OTPRegisterSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True, max_length=11, min_length=11, allow_blank=False,)

    def validated_phone(self, value:str):
        if not re.match(r'^09\d{9}$',value):
            raise serializers.ValidationError("Phone number is invalid: valid is 09xxxxxxxxx")
        return value

class OTPRegisterResponseSerializer(serializers.Serializer):
    timeout = serializers.IntegerField()


class OTPValidateSerializer(serializers.Serializer):
    code = serializers.CharField(required=True,allow_blank=False)
    phone = serializers.CharField(required=True, max_length=11, min_length=11, allow_blank=False,)

    def validated_phone(self, value:str):
        if not re.match(r'^09\d{9}$',value):
            raise serializers.ValidationError("Phone number is invalid: valid is 09xxxxxxxxx")
        return value


class OTPValidateResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
