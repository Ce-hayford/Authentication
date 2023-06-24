from django.db import models
from django.contrib.auth.models import AbstractUser

class signUser(AbstractUser):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200, unique=True)
    email = models.EmailField(unique=True)
    
    # password = models.CharField(max_length=200, unique=True, serialize=True)
    # confirmPassword = models.CharField(max_length=200, unique=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

