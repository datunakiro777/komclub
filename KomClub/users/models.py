from django.db import models

class User_info(models.Model):
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    gmail = models.CharField(max_length=255, unique=True)
    