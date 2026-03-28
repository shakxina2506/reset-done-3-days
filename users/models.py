from django.db import models
from django.contrib.auth.models import User


class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used=models.BooleanField(default=False)

    def __str__(self):
        return self.otp