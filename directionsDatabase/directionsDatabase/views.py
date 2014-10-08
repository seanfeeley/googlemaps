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
    
    area=Area.objects.filter(name="london")[0]
    lat,lon=area.getCenter()
    grid=PathGrid.objects.filter()[4]
    print grid
    
    points=Path.objects.filter(pathGrid=grid)
    print len(points)
    context = {'latitude': str(lat),'longitude':str(lon),'points':points}

    return render(request, 'maps/map.html',context)
