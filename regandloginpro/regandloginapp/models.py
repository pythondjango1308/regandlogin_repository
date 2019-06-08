from django.db import models
class RegistrationData(models.Model):
    first_name=models.CharField(max_length=50,default=" ")
    last_name=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    username=models.CharField(max_length=50)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)

