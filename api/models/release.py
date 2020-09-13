from django.db import models
from django.db.models import Model


class Release(Model):
    """This model represent any kind of release (Music, book, movie, tv show, etc)"""
    name = models.CharField(max_length=150)
    year = models.CharField(max_length=50)
    writer = models.CharField(max_length=100)
    plot = models.TextField()
    thumbnail = models.CharField(max_length=100)

    class Meta:
