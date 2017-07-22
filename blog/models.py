from django.db import models
from django.shortcuts import get_object_or_404
from diary_blog import settings


class PostManager(models.Manager):
    def create(self, *args, **kwargs):
        category_name = kwargs['categories']
        _category = get_object_or_404(Category, category=category_name)
        _category.counts += 1;
        _category.save()
        kwargs['categories'] = _category
        return super().create(*args, **kwargs)


class Post(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    text = models.TextField()
    written_date = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey('Category', blank=True, null=True)

    objects = PostManager()

    class Meta:
        ordering = ['-written_date']

    def __str__(self):
        return self.writer.name + ":" + self.title[:20]


class Category(models.Model):
    category = models.CharField(max_length=30)
    counts = models.IntegerField(default=0)

    def __str__(self):
        return self.category
