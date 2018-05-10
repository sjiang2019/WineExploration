from django.db import models

class Winery(models.Model):
    latitude = models.DecimalField(max_digits=5)
    longitude = models.DecimalField(max_digits=5)
    winery = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


    def __str__(self):
        return self.winery + ': ' + str(self.latitude) + ', ' + str(self.longitude)
