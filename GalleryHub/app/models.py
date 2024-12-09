from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


# Model to store images
class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    

# Model to store videos
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField() 
    created_at = models.DateTimeField(auto_now_add=True)


# Model to store audio files
class Audio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    audio_file = models.FileField() 
    created_at = models.DateTimeField(auto_now_add=True)


