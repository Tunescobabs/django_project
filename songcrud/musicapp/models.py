from datetime import datetime
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artist(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField()

    
class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE) #To show relationship btween Song and Aritist for song to be deleted when artist is deleted from th db
    title=models.CharField(max_length=50)
    date_released=models.DateField(default= datetime.today)
    likes=models.CharField(max_length=1000)
    artiste_id=models.IntegerField()

class Lyric(models.Model):
    content = models.CharField(max_length=1000)
    song_id =models.IntegerField()
    Song = models.OneToOneField(Song, on_delete = models.CASCADE, primary_key = True) # a lyric has one to one relationship with a song
