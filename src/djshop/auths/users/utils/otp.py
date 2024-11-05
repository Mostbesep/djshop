from random import randint

from django.conf import settings
from django.core.cache import cache


class OTPService:



    @staticmethod
    def validate_otp(mobile, received_otp):
        otp = cache.get(f'otp_{mobile}')
        if not otp or int(received_otp) != int(otp):
            return False
        return True


    @staticmethod
    def add_otp (mobile: str):
        code = (lambda: ''.join(str(randint(0, 9)) for _ in range(5)))()
        OTPService._send_otp(mobile,code)
        OTPService._set_otp_in_cache(code,mobile)

    @staticmethod
    def _set_otp_in_cache(otp: str, mobile: str):
        cache.set(f'otp_{mobile}', otp, timeout=settings.OTP_TIMEOUT)

    @staticmethod
    def _send_otp(mobile, otp):
        #TODO: Send OTP to mobile
        print('OTP sent to mobile number', mobile, otp)


    @staticmethod
    def _get_otp_from_cache(mobile: str):
        result = cache.get(f'otp_{mobile}')
        if result is not None:
            cache.delete(f'otp_{mobile}')
        return result