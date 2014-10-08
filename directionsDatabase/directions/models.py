from django.db import models
import math
# Create your models here.



class Area(models.Model):
    name = models.CharField(max_length=200)    
    topLeftLat = models.FloatField(default=0)
    topLeftLong = models.FloatField(default=0)
    bottomRightLat = models.FloatField(default=0)
    bottomRightLong = models.FloatField(default=0)
    def getCenter(self):
        return ((self.topLeftLat-self.bottomRightLat)/2+self.bottomRightLat,(self.topLeftLong-self.bottomRightLong)/2+self.bottomRightLong)

    def __unicode__(self):              
        return self.name


class LocationInArea(models.Model):
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    area = models.ForeignKey(Area)
    def __unicode__(self):
        lat=abs(self.area.topLeftLat-self.area.bottomRightLat)
        lon=abs(self.area.bottomRightLong-self.area.topLeftLong)
        percentLat=(float(abs(self.area.topLeftLat - self.latitude))/lat)*100
        percentLon=(float(abs(self.longitude-self.area.topLeftLong))/lon)*100
        
        return "%s, %d%% latitude, %d%% longitude"%(self.area.name, percentLat,percentLon)

class Location(models.Model):
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    name = models.CharField(max_length=200, default='')
    def __unicode__(self):              
        return self.name



class Departure(models.Model):
    time = models.DateTimeField('Departure time')
    def __unicode__(self):              
        return str(self.time)

class PathGrid(models.Model):
    departure = models.ForeignKey(Departure)

    location = models.ForeignKey(Location)
    area = models.ForeignKey(Area)

    fromLocationToArea = models.BooleanField(default=True)
    mode = models.CharField(max_length=200)

    density = models.IntegerField(default=0)
    
    def __unicode__(self):
        if self.fromLocationToArea:
            return "From %s to %s by %s at %s"%(self.location,self.area,self.mode,self.departure)
        else:
            return "From %s to %s by %s at %s"%(self.area,self.location,self.mode,self.departure)


class Path(models.Model):
    
    
    pathGrid = models.ForeignKey(PathGrid, default=0)

    locationInArea = models.ForeignKey(LocationInArea)


   
    seconds = models.IntegerField(default=0)
    delay = models.IntegerField(default=0)
    def __unicode__(self):

        mins=(self.seconds+self.delay)/60
        if mins>60:
            hours=mins/60.0
            timeString="%.2f hours"%hours
        else:
            timeString="%s mins"%mins

        mins=self.delay/60
        if mins>60:
            hours=mins/60.0
            timeDelayString="%.2f hours delay"%hours
        else:
            timeDelayString="%s mins delay"%mins 

        return "%s [%s] takes %s (%s)"%(self.pathGrid,self.locationInArea,timeString,timeDelayString)

