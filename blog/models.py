from django.db import models

from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=256)
    summary = models.TextField()
    cover_image = models.ImageField()
    content = models.TextField()
    content_cms = RichTextField(default="")
    status = models.CharField(
        max_length=32
    )
    published_date = models.DateField()
    slug = models.SlugField(max_length=264, default="")
