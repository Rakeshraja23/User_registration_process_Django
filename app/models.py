from django.db import models

# Create your models here.
from django.contrib.auth.models import User # providing path 

class profile(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.TextField()
    profile_pic = models.ImageField()


# Next process is to do the registration .