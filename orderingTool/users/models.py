from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("The given username is not valid.")

        if len(password) < 8:
            raise ValueError("The password must be at least 8 characters.")

        user = self.model(
            username = username,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        return self._create_user(username, password, **extra_fields)

    def create_staff_user(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=36, unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    objects = UserManager()

    # commented out to see purpose of 'class Meta'
    # class Meta:
    #     verbose_name = 'users'
    #     verbose_name_plural = 'Users'


def is_username_taken(attempted_name):
    """
    check for availability of the username
    """
    return User.objects.filter(username=attempted_name).exists()
