from django.db import models


class App(models.Model):
    name = models.CharField()
    description = models.CharField()
    url = models.UrlField()
    cover_image = models.ImageField()
    git_url = models.UrlField()
    youtube_url = models.UrlField()