from django.db import models
from diary_blog import settings


class Post(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    text = models.TextField()
    written_date = models.DateTimeField(auto_now_add=True)
    categories = models.OneToOneField('Category', blank=True, null=True)

    class Meta:
        ordering = ['-written_date']

    def __str__(self):
        return self.writer.username[:10] + ":" + self.title[:20]



class Category(models.Model):
    category = models.CharField(max_length=30)
    counts = models.IntegerField(default=0)
