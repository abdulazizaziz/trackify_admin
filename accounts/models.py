from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, name,  password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an Email")

        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """Create and save superuser"""

        if not email:
            raise ValueError("User must have email")

        user = self.model(email=email, name=name)

        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    def delete(self, *args, **kwargs):
        if not self.is_superuser:
            super().delete()

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.name


class UserSetting(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='setting')
    screenshot_delay = models.IntegerField()

    class Meta:
        db_table = 'usersetting'