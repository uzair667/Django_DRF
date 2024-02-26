from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50, default='')