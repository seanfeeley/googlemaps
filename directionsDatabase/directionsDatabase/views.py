from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse

from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def map(request):
	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('templates/maps/london.html')
    # context = RequestContext(request, {
    #     'latest_question_list': latest_question_list,
    # })
    return render(request, 'maps/london.html')
