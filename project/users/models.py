from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(blank = True , null = True)
    email = models.EmailField(unique=True)
    phone =  models.CharField(max_length=200,blank = True , null = True)
    GENDER_CHOICES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    ]
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, blank=True, null=True)
    address = models.CharField(max_length=200,blank = True , null = True)

    def __str__(self) -> str:
        return self.email