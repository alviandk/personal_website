from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    summary = models.TextField()
    cover_image = models.ImageField()
    content = models.TextField()
    status = models.CharField(
        max_length=32
    )
    published_date = models.DateField()
    slug = models.SlugField(max_length=264, default="")
