from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.TextField(max_length=40)
    desc = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'pk':self.pk})

