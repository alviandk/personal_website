from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    url = models.URLField()
    cover_image = models.ImageField()
    git_url = models.URLField()
    youtube_url = models.URLField()
    slug = models.SlugField(default="")
    ordering = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["ordering"]