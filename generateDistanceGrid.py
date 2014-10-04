import json, requests
import time
import sys,os
import json
import datetime
import argparse
sys.path.append("/Users/feeley19/coding/projects/googlemaps/directionsDatabase")
from pprint import pprint
os.environ["DJANGO_SETTINGS_MODULE"] = "directionsDatabase.settings"
# from django.contrib.auth.models import *
from directions.models import Area,LocationInArea,Location,Area,Departure,Path
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

def printLoadingBar(percentage):
    max=50
    print "[",

    for i in range(0,max):
        if float(i)/max<percentage:
            print 'I',
        else:
            print '-',
    print "]"

def loadFromJson(path):
    json_data=open(path)
    data = json.load(json_data)
    return data


def loadArea(name):
    area=Area.objects.filter(name=name)[0]
    return area

def loadPlace(name): 
    location=Location.objects.filter(name=name)[0]
    return location

def savePath():
    pass


def secondsToGetTo(home,dest,unix_time):

    time.sleep(2)
    seconds=-1
    url="https://maps.googleapis.com/maps/api/directions/json?origin=%f,%f&destination=%f,%f&key=AIzaSyCewGtfayH4MKxjtHpqJjpol8Q2dcKCDW8&&departure_time=%d&mode=transit"
    url= url%(home.latitude,home.longitude,dest[0],dest[1],unix_time)
    # print url
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    routes=data['routes']
    seconds=data['routes'][0]['legs'][0]['duration']['value']
    departure_time=data['routes'][0]['legs'][0]['departure_time']['value']
    delay=departure_time - unix_time
    return seconds + delay



def getGrid(area, place,gridDensity,unix_time):

    place=loadPlace(place)
    area=loadArea(area)

   

    # radius=0.2
    width=area.topLeftLat-area.bottomRightLat
    height=area.bottomRightLong-area.topLeftLong
    grid=[]

    for y in range(0,gridDensity):
        grid.append([])
        for x in range(0,gridDensity):
            printLoadingBar(float((y*gridDensity)+x)/float(gridDensity*gridDensity))
            loc=[area.topLeftLat-y*(height/(gridDensity-1)),area.topLeftLong+x*(width/(gridDensity-1))]
            seconds=secondsToGetTo(place,loc,unix_time)
            grid[y].append({'loc':loc,'seconds':seconds})

    return grid
   
    # seconds=secondsToGetTo(home,[home[0]+radius,home[1]])
    # mins=seconds/60
    

# if __name__ == '__main__':
#     # print sys.argv
def getGridAtTime(frm, to,day,hour,density):
    now = datetime.datetime.now()
    then = getNextDateTime(now,day,hour)
    unix_time = unixTime(then)
    return getGrid(to, frm,density,unix_time)

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
            print item['loc'],
        print 



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-day',default='friday')
    parser.add_argument('-hour',type=int,default='17')
    parser.add_argument('-to',default='london')
    parser.add_argument('-frm',default='home')
    parser.add_argument('-density',type=int,default='3')

   
    args = parser.parse_args()
    print "from %s to %s"%(args.frm, args.to)
    print "at %d:00 this %s"%(args.hour, args.day)
    print "rendering a %dx%d grid"%(args.density, args.density)
   
    grid=getGridAtTime(args.frm, args.to,args.day,args.hour,args.density)
    printGrid(grid)




