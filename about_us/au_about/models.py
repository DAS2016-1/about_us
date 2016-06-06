from django.db import models
from au_auth.models import Profile

# Create your models here.
class About(models.Model):
    comment = models.TextField()
    positive_votes = models.IntegerField()
    negative_votes = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

