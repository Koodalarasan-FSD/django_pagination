from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserRegistration(AbstractUser):
    dob = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=200, help_text='Required')
    country_code = models.CharField(max_length=10, blank=True, null=True)
    phoneNo = models.CharField(max_length=15, unique=True, blank=True, null=True)
    designation = models.CharField(max_length=30, blank=True, null=True)
    employeeId = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    status_cd = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=200, help_text='Required')
    address = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.username
