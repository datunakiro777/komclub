from django.db import models
from django.utils.text import slugify

class Events(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    participants = models.ManyToManyField('users.User_info', related_name='events')
    last_date = models.DateField()
    rules = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name