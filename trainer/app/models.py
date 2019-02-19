from django.db import models
import datetime
# Create your models here.


class info(models.Model):
    firstname= models.CharField(max_length=250)
    lastname= models.CharField(max_length=250)
    description= models.CharField(max_length=250,default='null')
    date=models.DateField()
    email = models.EmailField(max_length=20)
    def __str__(self):
        return self.firstname
