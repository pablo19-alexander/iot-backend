from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class IdentificationType(models.Model):
    name = models.CharField(max_length=50)


class User(AbstractUser):
    identification_type = models.ForeignKey(IdentificationType, on_delete=models.RESTRICT)
    identification = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=80, blank=True)

    objects = UserManager()  # Llama el objeto Gestor - agregar los atributos del BaseManager

    REQUIRED_FIELDS = ['first_name', 'last_name', 'identification_type', 'identification']


class Coordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    user_modifier = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='user_modifier')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

