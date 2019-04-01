from django.shortcuts import render,redirect

import time,re
# Create your views here.
from django.http import HttpResponse
from OJob.models import user,wkaddrs,reply,hangye,jobmge,leavemge,usernote
def base(request):
    userlist=user.objects.all()
    username = request.session.get('username')
    return render(request,'OJob/admin/user_mag.html',{'list1':userlist,'username':username})
def user_mag(request):
    username = request.session.get('username')
    userlist=user.objects.filter(uname=username)
    return render(request,'OJob/user/update_usernote.html',{'list':userlist})
def usernote_mag(request):
    username = request.session.get('username')
    usernotelist=usernote.objects.get("username")