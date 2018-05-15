# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# import uuid
from django.db import models
import bcrypt, re

# *******  TODO: convert back to UUID  ********

class UserManager(models.Manager):
    def validate(self, postData):
        print '******** UserManager: validate'
        print '******** UserManager: validate: postData', postData
        errors = []
        if len(postData['first_name']) < 2:
            errors.append("First name can not be blank")
        if not postData['first_name'].isalpha():
            errors.append("First name can not contain numbers")    
        
        if len(postData['last_name']) < 2:
            errors.append("Last name can not be blank")
        if not postData['last_name'].isalpha():
            errors.append("Last name can not contain numbers")          
        
        if len(postData['email']) < 1:
            errors.append("Email field can not be blank")
        if (User.objects.filter(email=postData['email'])):
            errors.append('Email already in use')

        if len(postData["password"]) < 8:
            errors.append("Password must be at least 8 characters")
        if postData["password"] != postData["password2"]:
            errors.append("Passwords do not match") 
        
        return errors

    def loginvalidate(self, postData): 
        # check db email with submitted email
        # print postData['email']
        errors = []
        
        if len(postData['email']) < 1:
            errors.append("Email field can not be blank")

        if len(postData["password"]) < 8:
            errors.append("Password must be at least 8 characters")
        else:
            bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt())    

        if (User.objects.filter(email=postData['email'])):
            print 'TRUE for emails'
            currentuser = User.objects.get(email=postData['email'])
            existingpwd = currentuser.password
            
            if not bcrypt.checkpw(postData["password"].encode(), existingpwd.encode()):
                errors.append("Password does not match")
        else:
            errors.append("Email does not match")
        
        return errors


class User(models.Model):
    
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()