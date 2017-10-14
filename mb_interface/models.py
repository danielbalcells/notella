# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Song(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    mbid = models.CharField(max_length=50)
    album = models.CharField(max_length=200)

    def __str__(self):
        return '"' + self.title + '", by ' + self.artist
