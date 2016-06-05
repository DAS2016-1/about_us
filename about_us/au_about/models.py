from django.db import models

# Create your models here.
class About(models.Model):
    comment = models.TextField()
    positive_votes = models.IntegerField()
    negative_votes = models.IntegerField()
