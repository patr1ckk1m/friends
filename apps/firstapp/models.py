# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validregister(self, post):
        errors = []

        if len(post['email']) < 1:
            errors.append("You must input an email")
        elif not EMAIL_REGEX.match(post['email']):
            errors.append("Invalid email address!")

        if len(post['name']) < 2:
            errors.append("You must input a valid name")
        if len(post['alias']) < 1:
            errors.append("Alias must be at least 2 characters")

        if len(post['password']) < 8:
            errors.append("Your pass must be longer than 8 characters")
        elif post['password'] != post['confirm']:
            errors.append("Your password does not match")

        if not errors:
            if User.objects.filter(email=post['email']):
                errors.append("Email already in use")
            else:
                hashed = bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt())
                user = User.objects.create(name=post['name'], alias=post['alias'], email=post['email'], password = hashed)
                return {"status": True, "user":user}

        return {"status": False, "errors": errors}

    def validlogin(self, post):
        errors = []
        if not User.objects.filter(email=post['loginemail']):
            errors.append("Invalid email")
        else:
            hashed = User.objects.get(email = post['loginemail']).password.encode('utf-8')
            password = post['loginpassword'].encode('utf-8')
            user = User.objects.get(email = post['loginemail'])
            # print bcrypt.hashpw(password, hashed)
            # print hashed
            if bcrypt.hashpw(password, hashed) == hashed:
                return {"status": True, "user": user}
            else:
                errors.append("Incorrect password")
        return {'status': False, 'errors':errors}

    def newFriend(self, user_id, friend_id):
        sender=User.objects.get(id=user_id)
        receiver=User.objects.get(id=friend_id)
        Friend.objects.create(user=sender, friend=receiver)
        Friend.objects.create(user=receiver, friend=sender)

    def removeFriend(self,user_id, friend_id):
        sender=User.objects.get(id=user_id)
        receiver=User.objects.get(id=friend_id)
        Friend.objects.get(user=sender, friend=receiver).delete()
        Friend.objects.get(user=receiver, friend=sender).delete()
class User(models.Model):
    name = models.CharField(max_length=26)
    alias = models.CharField(max_length=26)
    email = models.CharField(max_length=26)
    password = models.CharField(max_length=26)
    confirm = models.CharField(max_length=26)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Friend(models.Model):
    user = models.ForeignKey(User, related_name="sendrequest")
    friend = models.ForeignKey(User, related_name = 'receiverequest')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
