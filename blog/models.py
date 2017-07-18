from django.db import models
from user.models import BlogUser


class Blog(models.Model):
    writer = models.ForeignKey(BlogUser)
    text = models.TextField()
    written_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category')


class Category(models.Model):
    category = models.CharField(max_length=30)
