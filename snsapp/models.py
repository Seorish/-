from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.forms import DateTimeField


# 게시물 모델

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, blank=True, on_delete=models.CASCADE)
    # Post 를 참조하는 ForeignKey
    
    def __str__(self):
        return self.comment