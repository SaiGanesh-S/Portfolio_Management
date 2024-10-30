from django.db import models

# Create your models here.
class User_Account(models.Model):
    user_name = models.CharField(blank=False,max_length=50)
    user_email = models.EmailField(blank=False)
    user_phone = models.CharField(blank=False,max_length=10)
    user_profile_pic = models.ImageField(blank=True)