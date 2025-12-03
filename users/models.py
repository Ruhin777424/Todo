from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_vip = models.BooleanField(default=False)
    daily_limit = models.IntegerField(default=10)

    def save(self, *args, **kwargs):
        self.daily_limit = 30 if self.is_vip else 10
        super().save(*args, **kwargs)
