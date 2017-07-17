from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class BlogUserManager(BaseUserManager):
    def create_user(self, username, password, password2, name, phonenumber, sex=None):
        pass

    def create_superuser(self, username, password, password2, name, phonenumber):
        pass


class BlogUser(AbstractBaseUser):
    SEXES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    username = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=20)
