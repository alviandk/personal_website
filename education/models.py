from django.db import models


class School(models.Model):
    name = models.CharField(max_length=128)
    study = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    gpa = models.FloatField(null=True)


class GpaImage(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='gpa_images')
    file_image = models.ImageField()

class Thesis(models.Model):
    title = models.CharField(max_length=128)
    theme = models.CharField(max_length=128)
    url = models.URLField()
    # owner = models.ForeignKey()
    year = models.IntegerField()


class ThesisMentor(models.Model):
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE, related_name='mentors')

"""
S1 Skripsi
- Firda summaryzation
- Dita bepy
- Dea avcweb
- Noval 
- Alvian animetachi

S2 Tesis
- Nurul Test
- Alvian monte carlo pymc

S3 Doctor
- Yuhilza neupy

"""