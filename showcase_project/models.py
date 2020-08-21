from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    url = models.URLField()
    cover_image = models.ImageField()
    git_url = models.URLField()
    youtube_url = models.URLField()
    slug = models.SlugField(default="")