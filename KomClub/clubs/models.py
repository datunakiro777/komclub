from django.db import models
from users.models import User_info
from django.utils.text import slugify

class Clubs_info(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField('users.User_info', related_name='clubs', blank=True)
    owner = models.ForeignKey('users.User_info', related_name='owned_clubs', on_delete=models.CASCADE, default=1)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name