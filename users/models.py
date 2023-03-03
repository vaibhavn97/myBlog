from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='./profile_pics/default.png', upload_to='./profile_pics')
    first_name = models.CharField(max_length=27)
    last_name = models.CharField(max_length=27)
    bio = models.TextField()
    def __str__(self):
        return f"{self.user}"
