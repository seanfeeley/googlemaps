import json, requests
import time
import sys,os
import json
import datetime
import time
import argparse
sys.path.append("/Users/feeley19/coding/projects/googlemaps/directionsDatabase")
from pprint import pprint
os.environ["DJANGO_SETTINGS_MODULE"] = "directionsDatabase.settings"
# from django.contrib.auth.models import *
from directions.models import Area,LocationInArea,Location,Area,Departure,Path,PathGrid
import django


django.setup()

def getNextDateTime(now,day,hour):
    days={"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
    time = datetime.time(hour=hour)
    for key in days.keys():
        if key.startswith(day):
            dayNo=days[key]
    if now.time() < time:
        now = now.combine(now.date(),time)
    else:
        now = now.combine(now.date(),time) + datetime.timedelta(days=1)
    return now + datetime.timedelta((dayNo - now.weekday()) % 7)

def unixTime(datetime):
    return int(time.mktime(datetime.timetuple()))

def printLoadingBar(percentage,eta):
    max=50
    print "[",

    for i in range(0,max):
        if float(i)/max<percentage:
            print 'I',
        else:
            print '-',
    print "]",eta

def loadFromJson(path):
    json_data=open(path)
    data = json.load(json_data)
    return data

def makeLocationInArea(loc,area):
    locs=LocationInArea.objects.filter(area=area,latitude=loc[0],longitude=loc[1])
    if len(locs)==1:
        return locs[0]
    elif len(locs)==0:
        loc= LocationInArea(area=area,latitude=loc[0],longitude=loc[1])
        loc.save()
        return loc

def loadArea(name):
    area=Area.objects.filter(name=name)[0]
    return area



def loadPlace(name): 
    location=Location.objects.filter(name=name)[0]
    return location


def makeDeparture(time):
    departs=Departure.objects.filter(time=time)
    if len(departs)==1:
        return departs[0]
    elif len(departs)==0:
        depart= Departure(time=time)
        depart.save()
        return depart

def makePath(pathGrid,locationInArea,seconds,delay):
    paths=Path.objects.filter(pathGrid=pathGrid,locationInArea=locationInArea)
    if len(paths)==1:
        path=paths[0]
        path.seconds=seconds
        path.delay=delay
        path.save()
        return path

    elif len(paths)==0:
        path= Path(pathGrid=pathGrid,locationInArea=locationInArea,seconds=seconds,delay=delay)
        path.save()
        return path


def makePathGrid(location,area,fromLocationToArea,departure,mode):
    pathGrids=PathGrid.objects.filter(location=location,area=area,fromLocationToArea=fromLocationToArea,departure=departure,mode=mode)
    if len(pathGrids)==1:
        return pathGrids[0]
    elif len(pathGrids)==0:
        pathGrid= PathGrid(location=location,area=area,fromLocationToArea=fromLocationToArea,departure=departure,mode=mode)
        pathGrid.save()
        return pathGrid



def secondsToGetTo(pathGrid,loc):
    # return 999999,0
    time.sleep(2)
    seconds=-1


    if pathGrid.fromLocationToArea:
        fromLoc=pathGrid.location
        destLoc=loc
    else:
        fromLoc=loc
        destLoc=pathGrid.location
    
        
    unix_time = unixTime(pathGrid.departure.time)
    url="https://maps.googleapis.com/maps/api/directions/json?origin=%f,%f&destination=%f,%f&key=AIzaSyCewGtfayH4MKxjtHpqJjpol8Q2dcKCDW8&&departure_time=%d&mode=%s"
    url= url%(fromLoc.latitude,fromLoc.longitude,destLoc.latitude,destLoc.longitude,unix_time,pathGrid.mode)
    # print url
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    routes=data['routes']
    seconds=data['routes'][0]['legs'][0]['duration']['value']
    departure_time=data['routes'][0]['legs'][0]['departure_time']['value']
    delay=departure_time - unix_time
    
    

    return seconds,delay



def getGrid(area, place,gridDensity,depart,mode,fromLocationToArea):

    place=loadPlace(place)
    area=loadArea(area)

    pathGrid=makePathGrid(place,area,fromLocationToArea,depart,mode)
   

    # radius=0.2
    height=area.topLeftLat-area.bottomRightLat
    width=area.bottomRightLong-area.topLeftLong
    grid=[]

    for y in range(0,gridDensity):
        grid.append([])
        for x in range(0,gridDensity):
            time_marker=time.time()
            loc=[area.topLeftLat-y*(height/(gridDensity-1)),area.topLeftLong+x*(width/(gridDensity-1))]
            loc=makeLocationInArea(loc,area)
            
            seconds,delay=secondsToGetTo(pathGrid,loc)
            makePath(pathGrid,loc,seconds,delay)
            
            grid[y].append({'loc':loc,'seconds':seconds+delay})
            eta=time.time()-time_marker
            eta=eta*((gridDensity*gridDensity)-(1+(y*gridDensity)+x))
            if eta>120:
                eta="%d mins to go"%(eta/60)
            else:
                eta="%d seconds to go"%(eta)
            printLoadingBar(float((y*gridDensity)+x)/float(gridDensity*gridDensity),eta)


    return grid

    


def getGridAtTime(loc, area,day,hour,density,mode,toArea):
    now = datetime.datetime.now()
    then = getNextDateTime(now,day,hour)
    depart=makeDeparture(then)
    return getGrid(area, loc,density,depart,mode,toArea)

def printGrid(grid):
    for row in grid:
        for item in row:

            mins=item['seconds']/60
            if mins>60:
                hours=mins/60.0
                print "%.2f hours"%hours,
            else:
                print mins,"mins ",
        print 

    print
    for row in grid:
        for item in row:
            print item['loc'].latitude,item['loc'].longitude,"    ",
        print 



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-day',default='friday')
    parser.add_argument('-hour',type=int,default='17')
    parser.add_argument('-area',default='london')
    parser.add_argument('-loc',default='home')
    parser.add_argument('-mode',default='transit')
    parser.add_argument('-density',type=int,default='3')
    parser.add_argument('-toLocation',action='store_true',default=False)


   
    args = parser.parse_args()
    if args.toLocation:
        print "from %s to %s"%(args.area, args.loc)
    else:
        print "from %s to %s"%(args.loc, args.area)
    print "at %d:00 this %s"%(args.hour, args.day)
    print "rendering a %dx%d grid"%(args.density, args.density)
   
    grid=getGridAtTime(args.loc, args.area,args.day,args.hour,args.density,args.mode,not(args.toLocation))
    # printGrid(grid)




