from django.db import models

from ckeditor.fields import RichTextField

from my_journey.models import TechStack


BLOG_CATEGORY_CHOICES = [
    ("OPN","Opinion"),
    ("STY","Story"),
    ("RVW","Review"),
    ("TRL","Tutorial"),
    ("EXL","Explanation"),
]

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
    categoty = models.CharField(
        max_length=32, 
        choices=BLOG_CATEGORY_CHOICES, 
        default="STY"
    )
    tags = models.ManyToManyField(
        TechStack, 
        related_name='posts', 
        blank=True
    )
    slug = models.SlugField(max_length=264, default="")

    def __str__(self):
        return self.title
