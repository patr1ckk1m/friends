from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User, Friend

def index(request):
    return render(request, 'firstapp/index.html')

def friends(request):
    if not 'id' in request.session:
        del request.session
        return redirect('/')
    else:
        currentuser = User.objects.get(id=request.session['id'])
        users=User.objects.all()
        myFriends = []
        friends= Friend.objects.filter(user=currentuser)
        for each_friend in friends:
            myFriends.append(each_friend.friend)

        context = {
            'alias': User.objects.get(id=request.session['id']).alias,
            'users': users,
            'friends': myFriends
        }
    return render(request, 'firstapp/friends.html', context)

def register(request):
    res = User.objects.validregister(request.POST)
    if res["status"]:
        request.session['id'] = res['user'].id
        return redirect('/friends')
    else:
        for error in res["errors"]:
            messages.error(request, error)
        return redirect('/')

def login(request):
    res = User.objects.validlogin(request.POST)
    if res['status']:
        request.session['id'] = res['user'].id
        return redirect('/friends')
    else:
        for error in res["errors"]:
            messages.error(request, error)
        return redirect('/')

def viewprofile(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'firstapp/userprofile.html', context)

def addfriend(request, id):
    User.objects.newFriend(request.session['id'], id)
    return redirect('/friends')

def removefriend(request, id):
    User.objects.removeFriend(request.session['id'], id)
    return redirect('/friends')

def logout(request):
    request.session.pop('id')
    return redirect('/')
