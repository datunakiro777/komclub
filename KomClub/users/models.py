from django.db import models

class User_info(models.Model):
    username = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    gmail = models.EmailField(unique=True)
    pfp = models.ImageField(default='static/images/defaultpfp.jpg')
    def __str__(self):
        return self.username