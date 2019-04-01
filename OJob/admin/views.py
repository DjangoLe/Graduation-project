from django.shortcuts import render,redirect

import time,re
# Create your views here.
from django.http import HttpResponse
from OJob.models import user,wkaddrs,reply,hangye,jobmge,leavemge,usernote
def base(request):
    jmlist1=jobmge.objects.all()[0:4]
    return render(request,'OJob/admin/user_mag.html',{'list1':jmlist1})