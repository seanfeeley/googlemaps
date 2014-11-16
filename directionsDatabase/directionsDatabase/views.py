from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse

from django.shortcuts import render
from django.template import RequestContext, loader
import sys,os
sys.path.append(os.getcwd()+"../django-gmapi/")
# from gmapi import maps
# from gmapi.forms.widgets import GoogleMap
# Create your views here.
from directions.models import Area,LocationInArea,Location,Area,Departure,Path,PathGrid


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def map(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('templates/maps/london.html')
    # context = RequestContext(request, {
    #     'latest_question_list': latest_question_list,
    # })
    print request.path 
    map_name=str(request.path.split("/")[2])
    map_number=int(request.path.split("/")[3])-1

    area=Area.objects.filter(name="london")[0]
    lat,lon=area.getCenter()

    grid=PathGrid.objects.filter()[map_number]
    print grid
    
    points=Path.objects.filter(pathGrid=grid)
    validPoints=[]
    for point in points:
        if point.locationInArea.valid:
            validPoints.append(point)
    context = {'latitude': str(lat),'longitude':str(lon),'points':validPoints}

    # return render(request, 'maps/map.html',context)
    return render(request, 'maps/%s.html'%(map_name),context)
