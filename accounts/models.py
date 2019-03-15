from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class MyUsers(models.Model):
#     user = models.OneToOneField(User)
#     full_name = models.CharField(max_length=100, blank=True)
#     birthdate =models.DateField(null=True, blank=True)
#     father_name = models.CharField(max_length=100, blank=True)
#     Address = models.CharField(max_length=200, blank=True, null=True)
#     email = models.EmailField(max_length=100, blank=True, unique=True)
#     password = models.CharField(max_length=50)
#
#
#     def __str__(self):
#         return self.user.full_name