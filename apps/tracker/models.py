# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from datetime import date
from django.db import models

from ..login.models import User
# Create your models here.

class EventManager(models.Manager):
    def validateEvent(self, postData):
        print '********* got to EventManager'
        errors = []

        if len(postData['title']) < 2:
            errors.append("Title must be longer than 2 characters")

        if not postData['city'].isalpha():
            errors.append("City can not contain numbers")  

        if not postData['state'].isalpha():
            errors.append("State can not contain numbers")   

        # if len(postData['zip_code']).isalpha():  
        #     errors.append("Zip code must be numerals only") 

        if (postData['zip_code']) > 99999:  
            errors.append("Zip code must be 5 numbers")      

        # if postData['price'].isalpha():   
        #     errors.append("Price must be numerals only")

    # def inPast(self, postData):
    #     print "********* inPast validator, postdata: ", postData
    #     if self.date < date.today():
    #         date_error = []
    #         date_error.append("Date must be in the future")

        return errors

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    street = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    zip_code = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    participant = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EventManager()