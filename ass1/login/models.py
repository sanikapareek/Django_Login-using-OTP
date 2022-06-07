from django.db import models

# Create your models here.

class login(models.Model):
    phone=models.CharField(max_length=10)
    otp=models.AutoField(max_length=6)
