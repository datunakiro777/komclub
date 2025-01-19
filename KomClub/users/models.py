from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User_info(models.Model):
    username = models.CharField(max_length=15, default='bot')
    gmail = models.EmailField(unique=True)
    password = models.CharField(max_length=20, default='bot123')
    pfp = models.ImageField(default='../../static/images/defaultpfp.jpg')
    premmision = models.BooleanField(default=False)
    def __str__(self):
        return self.username