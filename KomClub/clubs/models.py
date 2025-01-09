from django.db import models
from users.models import User_info

class Clubs_info(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField('users.User_info', related_name='clubs', blank=True)
    owner = models.ForeignKey('users.User_info', related_name='owned_clubs', on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name    