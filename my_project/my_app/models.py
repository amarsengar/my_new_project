from django.db import models

# Create your models here.


class MyModels(models.Model):

    Name = models.CharField(max_length=50, blank=True)
    HostName = models.CharField(max_length=50, blank=True)
    

