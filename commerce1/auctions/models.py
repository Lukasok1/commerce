from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass
class category(models.Model):
    category = models.CharField(max_length = 30)
    def __str__ (self):
        return f"{self.category}"
class listing(models.Model):
    title = models.CharField(max_length=60)
    flActive = models.BooleanField(default=True)
    created_day = models.DateTimeField(default=timezone.now)
    description = models.CharField(null = True,max_length=300)
    starting_bid = models.FloatField()
class bid(models.Model):
    category = models.IntegerField(max_length=60)
    def __str__ (self):
        return f"{self.category}"
class comment(models.Model):
    comment_day = models.DateTimeField(default=timezone.now)
    comment = models.CharField(null = True,max_length=300)
class watchlist(models.Model):
    whatchlistlist = models.FloatField(max_length=60)

