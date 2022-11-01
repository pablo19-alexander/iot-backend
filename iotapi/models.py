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
    identification_type = models.ForeignKey(
        IdentificationType, on_delete=models.RESTRICT)
    identification = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=80, blank=True)

    objects = UserManager()  # Llama el objeto Gestor - agregar los atributos del BaseManager

    REQUIRED_FIELDS = ['first_name', 'last_name', 'identification_type', 'identification']

class Coordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    user_modifier = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name='user_modifier')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Vehicle(models.Model):
    id_vehicle = models.IntegerField(null=False, verbose_name="vehicle number ")
    vehicle_type = models.IntegerField(null=False, verbose_name="Type vehicle")
    vehicle_status = models.BooleanField('checked', default=True)
    license_plate = models.CharField(max_length=10)
    
class VehicleType(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    user_modifier = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='user_modifier_drive')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    company_card = models.CharField(max_length=80)
    drivers_license = models.CharField(max_length=15)
    drivers_license_state = models.DateField()
    
class Assignment(models.Model):
    user_modifier = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='user_modifier_assignment')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.RESTRICT)  
    conductor = models.ForeignKey(Driver, on_delete=models.RESTRICT)
    state = models.BooleanField('checked', default=True)


class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    user_modifer = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name='user_modifier_passenger')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    passenger_code = models.CharField(max_length=20, blank=True)
    passenger_permit = models.CharField(max_length=20, blank=True)

