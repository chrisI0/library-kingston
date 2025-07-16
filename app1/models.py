from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

class bookdetails(models.Model):
    name=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    copies=models.IntegerField()
    genre = models.CharField(max_length=20, null=True, blank=True)
    shelf = models.CharField(max_length=10, null=True, blank=True)
    level = models.CharField(max_length=5, null=True, blank=True)
    column = models.CharField(max_length=10, null=True, blank=True)
    
class borrow(models.Model):
    name = models.CharField(max_length=20)
    book_name = models.CharField(max_length=20, null=True, blank=True)
    copies = models.IntegerField()
    date_borrowed = models.DateField(default=datetime.now)