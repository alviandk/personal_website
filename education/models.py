from django.db import models


class School():
    name = models.CharField()
    study = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField()

class Thesis():
    title = models.CharField()
    theme = models.CharField()
    url = models.UrlField()
    owner = models.ForeignKey()
    year = models.IntegerField()


class ThesisMentor():
    thesis = models.ForeignKey(Thesis)
