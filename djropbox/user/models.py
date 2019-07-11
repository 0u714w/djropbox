from django.db import models
from django.contrib.auth.models import User


class BoxUser(models.Model):
    username = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
