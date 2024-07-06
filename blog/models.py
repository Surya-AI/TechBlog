from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Blog(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='blog_like')

    def numLikes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return '/'


class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='post_like')

    def numLikes(self):
        likes = self.likes.count()
        if likes:
            return likes
        else:
            return 0

