from django.db import models

# Create your models here.



class Area(models.Model):
    name = models.CharField(max_length=200)    
    topLeftLat = models.FloatField(default=0)
    topLeftLong = models.FloatField(default=0)
    bottomRightLat = models.FloatField(default=0)
    bottomRightLong = models.FloatField(default=0)
    def __unicode__(self):              
        return self.name


class LocationInArea(models.Model):
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    percentageAlongX = models.FloatField(default=0)
    percentageAlongY = models.FloatField(default=0)
    area = models.ForeignKey(Area)

class Location(models.Model):
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    name = models.CharField(max_length=200, default='')
    def __unicode__(self):              
        return self.name



class Departure(models.Model):
    time = models.DateTimeField('Departure time')
	

class Path(models.Model):
    arrival = models.DateTimeField('Arrival time')
    actualDeparture = models.DateTimeField('Actual departure time')
    
    departure = models.ForeignKey(Departure)

    location = models.ForeignKey(Location)
    locationInArea = models.ForeignKey(LocationInArea)


    mode = models.CharField(max_length=200)
    seconds = models.IntegerField(default=0)


