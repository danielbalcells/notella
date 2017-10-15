# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Basic model for a song containing artist, title, ID, and album.
class Song(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    mbid = models.CharField(max_length=50, primary_key=True)
    album = models.CharField(max_length=200)

    def __str__(self):
        render_string = '"' + self.title + '", by ' + self.artist
        return render_string.encode('utf-8')

# Basic model for a link between two songs. Contains FK relations to the two
# songs and a string explaining the connection.
class Link(models.Model):
    from_song = models.ForeignKey(Song, on_delete=models.CASCADE,
                related_name='from_song')
    to_song = models.ForeignKey(Song, on_delete=models.CASCADE,
                related_name='to_song')
    link_phrase = models.CharField(max_length=500)

    def __str__(self):
        render_string = str(self.from_song) + ' - ' + str(self.to_song)
        render_string += '. ' + self.link_phrase
        return render_string.encode('utf-8')
