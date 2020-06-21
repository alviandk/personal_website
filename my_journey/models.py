from django.db import models


class Company():
    name = models.CharField()
    url = models.UrlField()
    field = models.CharField()
    about = models.CharField()

class Experience():
    role = models.CharField()
    description = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField()


class Accomplishment():
    description = models.CharField()