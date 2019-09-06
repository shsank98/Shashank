from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=100,help_text="First Name")
    last_name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100,default="Guitar")

    def __str__(self):
        return self.first_name
class Album(models.Model):
    artist = models.ForeignKey(Musician,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name
