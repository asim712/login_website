from datetime import datetime
from operator import mod
from statistics import mode
from django.db import models


# Create your models here.
class Post(models.Model):
    img = models.ImageField(upload_to = 'pics')
    title = models.CharField(max_length=50)
    desc = models.TextField()
    created_at = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title
        
class About(models.Model):
    img = models.ImageField(upload_to = 'pics')
    title = models.CharField(max_length=100)
    high_title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.title
    

class Photo(models.Model):
    img = models.ImageField(upload_to = 'pics')

