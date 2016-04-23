from django.db import models
from tinymce.models import HTMLField

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    date = models.DateTimeField('Date')

    preview = HTMLField()
    content = HTMLField()

    read = models.IntegerField(default=0)

    def __str__(self):
        return self.title

