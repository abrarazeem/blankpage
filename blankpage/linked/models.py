from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TwitterAccount(models.Model):
    user = models.ForeignKey(User,unique=True)
    key = models.CharField(blank=False,max_length=255)
    secret = models.CharField(blank=False,max_length=255)
    type = models.BooleanField()
    twitter_id = models.IntegerField(max_length=11)
    screen_name = models.CharField(max_length=255)


class FacebookAccount(models.Model):
    user = models.ForeignKey(User,unique=True)
    access_token = models.CharField(max_length=255)
