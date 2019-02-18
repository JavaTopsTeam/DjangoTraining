from django.db import models

# Create your models here.
class newuser(models.Model):
    first_name = models.CharField(max_length = 20,db_index= True)
    last_name = models.CharField(max_length= 20)
    mobile = models.BigIntegerField(max_length=20)
    profile_pic = models.FileField(upload_to='images/',default='set.jpg')

    def __str__(self):
        return self.first_name +" " + self.last_name
