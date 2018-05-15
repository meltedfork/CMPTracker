# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import *

# Create your views here.

def viewEvent(request):
    return 

def newEvent(request):
    return render(request, 'tracker/addevent.html') 

def createEvent(request):
    errors = Event.objects.validateEvent(request.POST)
    # date_error = Event.objects.inPast(request.POST)
    # print '********** tracker date inPast error: ', date_error
    print '********* tracker Create Event errors: ', errors
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return HttpResponseRedirect('/new') 
    else:
        newevent = Event.objects.create(
            title = request.POST['title'],
            date = request.POST['date'],
            time = request.POST['time'],
            street = request.POST['street'],
            city = request.POST['city'],
            state = request.POST['state'],
            zip_code = request.POST['zip_code'],
            price = request.POST['price'],
        )   
        print '********* newevent method: ', newevent
    return HttpResponseRedirect('/dashboard')    

def allEvent(request):
    events = Event.objects.findAll()
    return render(request, 'login/dashboard.html', events)
    