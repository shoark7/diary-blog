from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class BlogUserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, username, password, name, phonenumber, sex='m'):

        username = self.model.normalize_username(username)
        user = self.model(username=username,
                          name=name,
                          phonenumber=phonenumber,
                          sex=sex,
                         )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, name, phonenumber, sex='m'):
        user = self.create_user(username, password, name, phonenumber, sex)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class BlogUser(AbstractBaseUser, PermissionsMixin):
    SEXES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    username = models.CharField(max_length=30, unique=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=1,
                           choices=SEXES,
                           default='m')
    is_supersuer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = BlogUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'phonenumber', 'sex']

    def __str__(self):
        return self.username + ': ' + self.name

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return self.__str__()


    # Future part. I'll add phonenumber validation 
    # def validate_unique(self, *args, **kwargs):
    #     super().super().validate_unique(*args, **kwargs)

