import datetime
from threading import Thread

from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import time,re
# Create your views here.
from django.http import HttpResponse
from ..models import *
from django.db.models import Q

#简历信息管理
def ManageResume(request):
    upower = request.session.get('upower')
    uname=request.session.get("username")
    lmlist = usernote.objects.filter(uname=uname)
    return render(request, 'OJob/user/ResumeManage.html', {"lmlist": lmlist, "upower": upower})
def ResumeOperation(request,id1,id2):
    uname = request.session.get("username")
    id1=int(id1)
    if id1==0:
       return render(request,'OJob/user/ResumeAdd.html',{"uname":uname})
    lmlist = usernote.objects.filter(id=id2).filter(uname=uname)
    return render(request,'OJob/user/ResumeUpdate.html',{'list':lmlist})
def AddResume(request):
    uname=request.POST.get("uname")
    realname = request.POST.get("realname")
    usex = request.POST.get("usex")
    uage= request.POST.get("uage")
    exp=request.POST.get("exp")
    telephone = request.POST.get("telephone")
    edubg = request.POST.get("edubg")
    if usernote.objects.filter(uname=uname).exists():
        return JsonResponse({"data": "error"})
    usernote.objects.create(uname=uname, realname=realname, usex=usex,uage=uage,exp=exp,telephone=telephone,edubg=edubg)
    return JsonResponse({"data": "success"})

def UpdateResume(request):
    uname = request.POST.get("uname")
    realname = request.POST.get("realname")
    usex = request.POST.get("usex")
    uage = request.POST.get("uage")
    exp = request.POST.get("exp")
    telephone = request.POST.get("telephone")
    edubg = request.POST.get("edubg")
    obj = usernote.objects.get(uname=uname)
    obj.realname=realname
    obj.usex=usex
    obj.exp=exp
    obj.uage=uage
    obj.telephone=telephone
    obj.edubg=edubg
    obj.save()
    return JsonResponse({"data":"success"})

#投递情况管理
def ManageDeliver(request,id):
    upower = request.session.get('upower')
    uname = request.session.get("username")
    lmlist=""
    if reply.objects.filter(uname=uname).exists():
        lmlist=reply.objects.filter(uname=uname)
    paginator = Paginator(lmlist, 4)
    id = int(id)
    if id < 1:
        id = 1
    try:
        lmlist = paginator.page(id)
    except EmptyPage:
        id = paginator.num_pages
        lmlist = paginator.page(paginator.num_pages)
    return render(request, 'OJob/user/DeliverManage.html', {"lmlist": lmlist, "upower": upower, "id": id})
def DeliverOperation(request,id1,id2):
    uname = request.session.get("username")
    return render(request,'OJob/user/DeliverAdd.html',{"uname":uname})

def AddDeliver(request):
    uname = request.POST.get("uname")
    cpname = request.POST.get("cpname")
    jposition= request.POST.get("jposition")
    if reply.objects.filter(uname=uname,epname=cpname).exists():
        return JsonResponse({"data": "error"})
    if not company.objects.filter(cname=cpname).exists() and jobmge.objects.filter(jposition=jposition).exists():
        return JsonResponse({"data": "error1"})
    reply.objects.create(uname=uname, epname=cpname, jposition=jposition)
    return JsonResponse({"data": "success"})

def DeleteDeliver(request):
    id = request.POST.get("id")
    reply.objects.filter(id=id).delete()
    return JsonResponse({"tips": "删除成功"})
def DeleteAllDeliver(request):
    list1 = request.POST.getlist("list1[]")
    for i in list1:
        reply.objects.filter(id=i).delete()
    return JsonResponse({"tips": "删除成功"})


def QueryDeliver(request):
    upower = request.session.get('upower')
    jposition = request.POST.get("jposition")
    epname = request.POST.get("company")
    uname = request.session.get("username")
    print("***********")
    if jposition=="" and epname=="":
        lmlist=None
    elif jposition=="":
        lmlist=reply.objects.filter(Q(epname__contains=epname),uname=uname)
    elif epname=="":
        lmlist = reply.objects.filter(Q(jposition__contains=jposition),uname=uname)
    else:
        lmlist=reply.objects.filter(Q(epname__contains=epname) & Q(jposition__contains=jposition),uname=uname)
    return render(request,'OJob/user/DeliverManage.html',{"lmlist":lmlist,"upower":upower,"id":1})

#职位薪资分布
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import pandas as pd

def PlaceDistribute(request):
    cityList=[]
    upower = request.session.get('upower')
    clist=jobmge.objects.all()
    for item in clist:
        cityList.append(item.jplace)
    seriesInfo = pd.Series(cityList).value_counts().head(6).sort_values(ascending=False).plot(kind='bar',color=['r','g','b','y','m'])
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("招聘地区分布")
    plt.xlabel("地区")
    plt.ylabel("招聘数量")
    plt.xticks(rotation=1)
    plt.savefig("static/admin/img/place.jpg",bbox_inches='tight')
    plt.close()
    return render(request,'OJob/user/PlaceDistribute.html',{"upower":upower})
def PositionDistribute(request):
    PositionList = []
    upower = request.session.get('upower')
    clist = jobmge.objects.all()
    for item in clist:
        PositionList.append(item.jposition)
    # plt.figure(figsize=(8, 6))
    #pandas自带绘图函数，它是以matplotlib包为基础封装，所以两者能够结合使用
    #value_counts():用于计算一个Series中各值出现的频率
    #Series():Series类型由一组数据及与之相关的数据索引组成,index与列表元素个数一致
    seriesInfo = pd.Series(PositionList).value_counts().head(6).sort_values(ascending=False).plot(kind='bar', color=['r', 'g', 'b','y','m'])
    # print(pd.Series(PositionList))
    # print("---------------------")
    # print(pd.Series(PositionList).value_counts())
    # print(pd.Series(PositionList).value_counts().head(5))
    # print(pd.Series(PositionList).value_counts().head(5).sort_values(ascending=False))
    plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False#用来正常显示负号
    plt.title("招聘职位分布")
    plt.xlabel("职位")
    plt.ylabel("招聘数量")
    plt.xticks(rotation=1)
    plt.savefig("static/admin/img/position.jpg",bbox_inches='tight')
    plt.close()
    return render(request, 'OJob/user/PositionDistribute.html', {"upower": upower})