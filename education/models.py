from django.db import models


class School(models.Model):
    name = models.CharField()
    study = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField()

class Thesis(models.Model):
    title = models.CharField()
    theme = models.CharField()
    url = models.UrlField()
    owner = models.ForeignKey()
    year = models.IntegerField()


class ThesisMentor(models.Model):
    thesis = models.ForeignKey(Thesis)
