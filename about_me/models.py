from django.db import models


class Description(models.Model):
    short_version = models.CharField(max_length=128)
    long_version = models.TextField()


class ProfilePicture(models.Model):
    file = models.ImageField()


class PersonalInformation(models.Model):
    email = models.EmailField()
    location = models.CharField(max_length=64)
    website = models.URLField()
    linkedin = models.URLField()
    github = models.URLField()