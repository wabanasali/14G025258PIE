from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    post_title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date =  models.DateTimeField()
    published_date =  models.DateTimeField()