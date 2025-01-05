from django.db import models
from users.models import User_info

class Clubs_info(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(User_info, related_name='clubs', blank=True)
    owner = models.ForeignKey(User_info, on_delete=models.CASCADE, related_name='owned_clubs', default=1)
    def __str__(self):
        return self.name