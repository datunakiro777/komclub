from django.db import models

class User_info(models.Model):
    username = models.CharField(max_length=155, unique=True)
    password = models.CharField(max_length=155)
    gmail = models.EmailField(unique=True)

    def __str__(self):
        return self.username
