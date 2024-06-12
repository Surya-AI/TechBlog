from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    about = models.TextField(default='Hi, I am new to TechBlog')
    gender = models.TextField(default='None')
    dob = models.DateField(default='1999-01-01')
    # image = models.ImageField(default='default.png', name='profile_pic', upload_to='profile_pics')
    

    def __str__(self):
        return f"{self.user.username}'s Profile"
