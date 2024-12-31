from django.db import models
from users.models import User_info

class Clubs_info(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    members = models.ManyToManyField('User_info.username', related_name='clubs')