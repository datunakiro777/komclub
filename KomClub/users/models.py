from django.db import models

class User_info(models.Model):
    username = models.CharField(max_length=15, unique=True, null=True)
    gmail = models.EmailField(unique=True)
    pfp = models.ImageField(default='static/images/defaultpfp.jpg')
    def __str__(self):
        return self.username