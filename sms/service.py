from django.core.mail import send_mail
from django.conf import settings


def send_otp(email, otp):
    send_mail(
        subject=f'OTP verify account',
        message=f' Your OTP is  {otp}\n it will expire 5 minutes',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )