from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)           
    mobile = models.IntegerField(max_length=12)