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
    # comments = models.ManyToManyField(Comment, related_name='blog_comment')

    def numLikes(self):
        return self.likes.count()

    # def numComments(self):
    #     return self.comments.count()

    def get_absolute_url(self):
        return '/'


class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='post_like')
    # comments = models.ManyToManyField(Comment, related_name='post_comment')

    def numLikes(self):
        likes = self.likes.count()
        if likes:
            return likes
        else:
            return 0

    def numComments(self):
        return self.comments.count()


class PostComment(models.Model):
    content = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)


class BlogComment(models.Model):
    content = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='blog_comment_like')

    def numLikes(self):
        return self.likes.count()