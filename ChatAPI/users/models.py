from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    pass

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
