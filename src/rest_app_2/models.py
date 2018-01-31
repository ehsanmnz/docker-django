from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=1024)
    text = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments")
    text = models.TextField()
    active = models.BooleanField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.text
