from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    int_number = models.IntegerField()

    def __str__(self):
        return str(self.user)
