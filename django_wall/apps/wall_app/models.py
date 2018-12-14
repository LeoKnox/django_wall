from __future__ import unicode_literals

from django.db import models
import bcrypt, re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["fname"]) < 3:
            errors["fname"] = "First name should be at least 2 characters"
        if len(postData["lname"]) < 3:
            errors["lname"] = "Last name should be at least 2 characters"
        if postData["password"] != postData["confirmpass"]:
            errors["passwords"] = "Passwords must match"
        if postData["password"] < 9:
            errors["password"] = "Password must be at least 8 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData["email"]):
            errors["snail"] = "Invalid Email"
        check = User.objects.filter(email=postData["email"])
        if len(check)>0:
            errors["duplicate"] = "Email in use, please choose another"
        return errors
    
    def pw_validator(self, postData):
        errors = {}
        check = User.objects.filter(email=postData["email"])
        if len(check)>0:
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            hpd = check[0].password
            if not EMAIL_REGEX.match(postData["email"]):
                errors["snail"] = "Invalid Email"
            if not bcrypt.checkpw(postData["password"].encode(), hpd.encode()):
                errors["login"] = "Incorrect user/password"
            print (errors)
        else:
            errors["hail"] = "Try another Email"
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = UserManager()

 #-------------- wall code here
class Message(models.Model):
    message=models.TextField()
    creator=models.ForeignKey(User, related_name="user_id")
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment=models.TextField()
    commenter=models.ForeignKey(User, related_name="commenter_id")
    commment_message=models.ForeignKey(Message, related_name="message_id")
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
# Create your models here.
