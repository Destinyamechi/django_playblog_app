from django.db import models
from user.models import CustomUser
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null = True, blank = True)
    last_name = models.CharField(max_length=100, null = True, blank = True)
    age = models.CharField(max_length=100, null = True, blank = True)
    address = models.CharField(max_length=100, null = True, blank = True)
    phone_number = models.CharField(max_length=100, null = True, blank = True)
    
    def __str__(self):
        return f"{self.user}|{self.first_name}"