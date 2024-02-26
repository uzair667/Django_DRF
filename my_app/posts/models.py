from django.db import models
from crud.models import Users
from my_app.exceptions import UnprocessableEntity
from django.db.models.signals import pre_delete
from django.dispatch import receiver
# Create your models here.


class Posts(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)



@receiver(pre_delete, sender = Users)
def prevent_delete_for_user(sender, instance, **kwargs):
    if instance.posts_set.exists():
        raise UnprocessableEntity("cannot delete user contains data in posts")