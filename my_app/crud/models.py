from django.db import models


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50, default='')

class Posts(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)