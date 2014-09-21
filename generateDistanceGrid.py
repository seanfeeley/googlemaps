import json, requests
import time
import sys,os
import json
import datetime
import argparse


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
    return loadFromJson("./locations/areas/%s.json"%(name))

def loadPlace(name):
    return loadFromJson("./locations/places/%s.json"%(name))


def secondsToGetTo(home,dest):

    time.sleep(2)
    seconds=-1
    url="https://maps.googleapis.com/maps/api/directions/json?origin=%f,%f&destination=%f,%f&key=AIzaSyCewGtfayH4MKxjtHpqJjpol8Q2dcKCDW8&&departure_time=%d&mode=transit"
    url= url%(home[0],home[1],dest[0],dest[1],time.time())
    # print url
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    routes=data['routes']
    seconds=data['routes'][0]['legs'][0]['duration']['value']
 
    
    return seconds



def getGrid(area, place,gridDensity):

    place=loadPlace(place)
    area=loadArea(area)

    topLeft=area[0]
    bottomRight=area[1]

    # radius=0.2
    width=topLeft[0]-bottomRight[0]
    height=bottomRight[1]-topLeft[1]
    grid=[]

    for y in range(0,gridDensity):
        grid.append([])
        for x in range(0,gridDensity):
            printLoadingBar(float((y*gridDensity)+x)/float(gridDensity*gridDensity))
            loc=[topLeft[0]-y*(height/(gridDensity-1)),topLeft[1]+x*(width/(gridDensity-1))]
            seconds=secondsToGetTo(place,loc)
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
    return getGrid(to, frm,density)

def printGrid(grid):
    for row in grid:
        for item in row:
            print item['seconds']/60,
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




