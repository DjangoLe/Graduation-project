import datetime
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import time,re
# Create your views here.
from django.http import HttpResponse
from django.db.models import Q

from ..models import *

#企业信息管理
def ManageComInfo(request):
    upower = request.session.get('upower')
    uname=request.session.get('username')
    cpname=""
    id=user.objects.filter(uname=uname).values("id")
    cplist=company.objects.filter(createid=id)
    for item in cplist:
        cpname=item.cname
    request.session["cpname"]=cpname
    print("************1111")
    print(cpname)
    return render(request,"OJob/company/CompanyManage.html",{"cplist":cplist,"upower":upower,"createname":uname})


#企业招聘信息管理
def ManageRecruitInfo(request,id):
    upower = request.session.get('upower')
    uname = request.session.get('username')
    cpname = ""
    id1 = user.objects.filter(uname=uname).values("id")
    cplist = company.objects.filter(createid=id1)
    for item in cplist:
        cpname = item.cname
    request.session["cpname"]=cpname
    lmlist = jobmge.objects.filter(epname=cpname)
    paginator = Paginator(lmlist, 4)
    id = int(id)
    if id < 1:
        id = 1
    try:
        lmlist = paginator.page(id)
    except EmptyPage:
        id = paginator.num_pages
        lmlist = paginator.page(paginator.num_pages)
    return render(request, 'OJob/company/RecruitInfoManage.html', {"lmlist": lmlist, "upower": upower, "id": id})
def RecruitInfoOperation(request,id1,id2):
    cpname = request.session.get("cpname")
    id1=int(id1)
    if id1==0:
       return render(request,'OJob/company/RecruitInfoAdd.html',{"cpname":cpname})
    lmlist = jobmge.objects.filter(id=id2).filter(epname=cpname)
    return render(request,'OJob/company/RecruitInfoUpdate.html',{'list':lmlist})
def AddRecruitInfo(request):
    epname=request.POST.get("epname")
    clist=company.objects.filter(cname=epname)
    for item in clist:
        epid=item.id
    jposition = request.POST.get("jposition")
    jplace = request.POST.get("jplace")
    jwages= request.POST.get("jwages")
    jcount=request.POST.get("jcount")
    jskill = request.POST.get("jskill")
    workexp = request.POST.get("workexp")
    jobmge.objects.create(epname=epname, epid=epid,jposition=jposition, jplace=jplace,jwages=jwages,jcount=jcount,jskill=jskill,workexp=workexp, settime=datetime.datetime.now())
    return JsonResponse({"data": "success"})

def UpdateRecruitInfo(request):
    epname = request.POST.get("epname")
    jposition = request.POST.get("jposition")
    jplace = request.POST.get("jplace")
    jwages = request.POST.get("jwages")
    jcount = request.POST.get("jcount")
    jskill = request.POST.get("jskill")
    workexp = request.POST.get("workexp")
    obj = jobmge.objects.get(epname=epname,jposition=jposition)
    obj.jposition=jposition
    obj.jplace=jplace
    obj.jwages=jwages
    obj.jcount=jcount
    obj.jskill=jskill
    obj.workexp=workexp
    obj.save()
    return JsonResponse({"data":"success"})
def DeleteRecruitInfo(request):
    id = request.POST.get("id")
    jobmge.objects.filter(id=id).delete()
    return JsonResponse({"tips": "删除成功"})
def DeleteAllRecruitInfo(request):
    list1 = request.POST.getlist("list1[]")
    for i in list1:
        jobmge.objects.filter(id=i).delete()
    return JsonResponse({"tips": "删除成功"})
def QueryRecruitInfo(request):
    upower = request.session.get('upower')
    position = request.POST.get("position")
    place = request.POST.get("place")
    cpname = request.session.get('cpname')
    if position=="" and place=="":
        lmlist=None
    elif position=="":
        lmlist=jobmge.objects.filter(Q(jplace__contains=place),epname=cpname)
        print(place)
        print("***********")
        print(lmlist)
    elif place=="":
        lmlist = jobmge.objects.filter(Q(jposition__contains=position),epname=cpname)
    else:
        lmlist=jobmge.objects.filter(Q(jplace__contains=place) & Q(jposition__contains=position),epname=cpname)
    return render(request,'OJob/company/RecruitInfoManage.html',{"lmlist":lmlist,"upower":upower,"id":1})

#审核信息管理
def ManageAudit(request,id):
    upower = request.session.get('upower')
    uname = request.session.get("username")
    cpname = ""
    id1 = user.objects.filter(uname=uname).values("id")
    cplist = company.objects.filter(createid=id1)
    for item in cplist:
        cpname = item.cname
    lmlist=""
    if reply.objects.filter(epname=cpname).exists():
        lmlist=reply.objects.filter(epname=cpname)
    paginator = Paginator(lmlist, 4)
    id = int(id)
    if id < 1:
        id = 1
    try:
        lmlist = paginator.page(id)
    except EmptyPage:
        id = paginator.num_pages
        lmlist = paginator.page(paginator.num_pages)
    return render(request, 'OJob/company/AuditManage.html', {"lmlist": lmlist, "upower": upower, "id": id})
#查看简历信息
def AuditOperation(request,id1,id2):
    list = reply.objects.filter(id=id2)
    for item in list:
        uname=item.uname
    rlist=reply.objects.filter(id=id2)
    unlist=usernote.objects.filter(uname=uname)
    print("*+++++++++++++++++++++")
    id1=int(id1)
    if id1==0:
        return render(request,'OJob/company/ResumeView.html',{"unlist":unlist})
    if id1==1:
        return render(request, 'OJob/company/ReplyUser.html', {"rlist": rlist})
def AddAudit(request):
    id = request.POST.get("id")
    uname = request.POST.get("uname")
    cpname = request.POST.get("cpname")
    substance=request.POST.get("substance")
    object=reply.objects.get(id=id,uname=uname,epname=cpname)
    object.substance=substance
    object.save()

    return JsonResponse({"data": "success"})

def HandleAudit(request):
    id = request.POST.get("id")
    rlist=reply.objects.filter(id=id)
    isenter=1
    for item in rlist:
        isenter=item.isenter
        if isenter==1:
            isenter=2
        else:
            isenter=1
    object=reply.objects.get(id=id)
    object.isenter=isenter
    object.save()
    return JsonResponse({"tips": "删除成功"})
def DeleteAllAudit(request):
    list1 = request.POST.getlist("list1[]")
    for i in list1:
        object =reply.objects.get(id=i)
        object.isenter = 2
        object.save()
    return JsonResponse({"tips": "删除成功"})


def QueryAudit(request):
    cpname = request.session.get('cpname')
    upower = request.session.get('upower')
    jposition = request.POST.get("jposition")
    uname = request.POST.get("uname")
    if jposition=="" and uname=="":
        lmlist=None
    elif jposition=="":
        lmlist=reply.objects.filter(Q(uname__contains=uname),epname=cpname)
    elif uname=="":
        lmlist = reply.objects.filter(Q(jposition__contains=jposition),epname=cpname)
    else:
        lmlist=reply.objects.filter(Q(uname__contains=uname) & Q(jposition__contains=jposition),epname=cpname)
    return render(request,'OJob/company/AuditManage.html',{"lmlist":lmlist,"upower":upower,"id":1})
