from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, professor_id, password=None, **extra_fields):
        if not professor_id:
            raise ValueError("Professor ID is required")
        user = self.model(professor_id=professor_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, professor_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(professor_id, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    professor_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = CustomUserManager()
    USERNAME_FIELD = 'professor_id'
    REQUIRED_FIELDS = ['full_name', 'email']

    def __str__(self):
        return self.professor_id

