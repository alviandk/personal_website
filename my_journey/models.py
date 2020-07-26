from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField()
    field = models.CharField(max_length=64)
    about = models.CharField(max_length=128)


class Accomplishment(models.Model):
    description = models.CharField(max_length=128)


class Experience(models.Model):
    role = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='experiences')
    accomplishment = models.ManyToManyField(Accomplishment, related_name='experiences', blank=True)
