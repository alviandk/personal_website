from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField()
    field = models.CharField(max_length=64)
    about = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Accomplishment(models.Model):
    description = models.CharField(max_length=128)


class Experience(models.Model):
    role = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='experiences')
    accomplishment = models.ManyToManyField(Accomplishment, related_name='experiences', blank=True)

    def __str__(self):
        return f'{self.role} - {self.company}'


class Competition(models.Model):
    description = models.CharField(max_length=128)


class Certificate(models.Model):
    image = models.ImageField()
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='certificates')


class TechStack(models.Model):
    name = models.CharField(max_length=64)
    svg = models.TextField()

    def __str__(self):
        return self.name