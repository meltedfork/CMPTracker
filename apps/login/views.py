# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import bcrypt
from .models import *


def index(request):
    if 'userid' in request.session:
       return HttpResponseRedirect('/dashboard') 
    else:
        print 'error messages here from index'
    return render(request, 'login/login.html')

def hello_world(request):
    return render(request, 'hello/world.html') 

def register(request):
    errors = User.objects.validate(request.POST)
    print "****** register errors: ", errors
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        # return redirect('/')
        return HttpResponseRedirect('/') 
    else:
        hashpwd = bcrypt.hashpw(
        request.POST["password"].encode(), bcrypt.gensalt())
        newuser = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hashpwd)
    request.session['userid'] = newuser.id
    request.session['name'] = newuser.first_name
    print "*******session info", newuser.id, newuser.first_name
    # TODO: figure out why redirect('/dashboard') does not work
    return HttpResponseRedirect('/dashboard') 

def login(request):
    errors = User.objects.loginvalidate(request.POST)
    print "**********login errors: ", errors
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return HttpResponseRedirect('/')
    else:
        user = User.objects.filter(email=request.POST['email'])[0]
        print "******login user", user
        print "*******user.id:", user.id
        request.session['userid'] = user.id
        request.session['name'] = user.first_name
        return HttpResponseRedirect('/dashboard')    

def dashboard(request):
    print '*********** Success point here'
    print request.session['name']
    return render(request, 'login/dashboard.html')    

def logout(request):
    request.session.clear()
    print 'goodbye'
    return HttpResponseRedirect('/')   
   
