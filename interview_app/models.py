from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_Teacher = models.BooleanField(default=False)
    is_Student = models.BooleanField(default=False)


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    email = models.TextField(max_length=50)
    contact = models.IntegerField()
    image = models.ImageField(upload_to='pic')
