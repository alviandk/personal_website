from django.db import models


class Description(models.Model):
    short_version = models.CharField()
    long_version = models.TextField()


class ProfilePicture():
    file = models.ImageField()


class PersonalInformation():
    email = models.CharField()
    location = models.CharField()
    website = models.CharField()
    linkedin = models.UrlField()
    github = models.UrlField()