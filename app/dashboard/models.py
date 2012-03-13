from django.db import models

# Create your models here.
class Client(models.Model):
    oauth_token = models.CharField(blank=False,max_length=255)
    oauth_token_secret = models.CharField(blank=False,max_length=255)
    verified = models.BooleanField()


