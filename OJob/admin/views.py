import datetime
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import time,re
# Create your views here.
from django.http import HttpResponse
from ..models import *
from django.db.models import Q

#个人信息管理
def MyManage(request):
    upower = request.session.get('upower')
    username = request.session.get('username')
    userlist=user.objects.filter(uname=username)
    return render(request,'OJob/admin/MyManage.html',{"upower":upower,"userlist":userlist})
def UpdatePasswd(request,id):
    userlist=user.objects.filter(id=id)
    for item in userlist:
        uname=item.uname
    return render(request,'OJob/admin/UpdatePasswd.html',{"uname":uname})
def UpdateUserPasswd(request):
    uname = request.POST.get("username")
    passwd = request.POST.get("pass")
    print("ssssssssssssssssssssssssssssssss")
    print(uname)
    object=user.objects.get(uname=uname)
    object.upasswd=passwd
    object.save()
    return JsonResponse({"date":"success"})
def AddUser(request):
        uname = request.POST.get("username")
        passwd = request.POST.get("pass")
        tel = request.POST.get("phone")
        addrs = request.POST.get("address")
        if user.objects.filter(uname=uname).exists():
            return JsonResponse({"data": "error"})
        user.objects.create(uname=uname, upasswd=passwd, telephone=tel, uaddress=addrs)
        return JsonResponse({"data": "success"})
#用户信息管理
def Manage_user(request,id):
    upower= request.session.get('upower')
    userlist=user.objects.filter(upower__gt=0)
    paginator = Paginator(userlist, 4)
    id=int(id)
    if id<1:
        id=1
    try:
        list=paginator.page(id)
    except EmptyPage:
        id=paginator.num_pages
        list = paginator.page(paginator.num_pages)
    return render(request,'OJob/admin/UserManage.html',{"upower":upower,"userlist":list,"id":id})
def UserOperation(request,id1,id2):
    id1=int(id1)
    if id1==0:
       return render(request,'OJob/admin/UserAdd.html')
    userlist = user.objects.filter(id=id2)
    return render(request,'OJob/admin/UserUpdate.html',{'list':userlist})
def UpdateUser(request):
    uname = request.POST.get("username")
    tel = request.POST.get("phone")
    addrs = request.POST.get("address")
    if user.objects.filter(uname=uname).exists()==False:
        return JsonResponse({"tips": "错误"})
    obj = user.objects.get(uname=uname)
    obj.telephone = tel
    obj.uaddress = addrs
    obj.save()
    return JsonResponse({"tips": "修改成功"})
def DeleteUser(request):
    id = request.POST.get("id")
    user.objects.filter(id=id).delete()
    return JsonResponse({"tips":"删除成功"})

def QueryUser(request):
    upower = request.session.get('upower')
    id = request.POST.get("id")
    uname = request.POST.get("username")
    if id=="" and uname=="":
        userlist=None
    elif uname=="":
        userlist=user.objects.filter(Q(id__contains=id)).exclude(upower=0)
    elif id=="":
        userlist = user.objects.filter(Q(uname__contains=uname)).exclude(upower=0)
    else:
        userlist=user.objects.filter(Q(id__contains=id) & Q(uname__contains=uname)).exclude(upower=0)
    return render(request,'OJob/admin/UserManage.html',{"userlist":userlist,"upower":upower,"id":1})


def DeleteAllUser(request):
    list1=request.POST.getlist("list1[]")
    for i in list1:
        user.objects.filter(id=i).delete()
    return JsonResponse({"tips":"删除成功"})

#企业信息管理
def ManageCompany(request,id):
    upower = request.session.get('upower')
    cplist=company.objects.all()
    paginator = Paginator(cplist, 4)
    id = int(id)
    if id < 1:
        id = 1
    try:
        cplist = paginator.page(id)
    except EmptyPage:
        id = paginator.num_pages
        cplist = paginator.page(paginator.num_pages)
    return render(request,'OJob/admin/CompanyManage.html',{"cplist":cplist,"upower":upower,"id":id})
def CompanyOperation(request,id1,id2):
    id1=int(id1)
    if id1==0:
       return render(request,'OJob/admin/CompanyAdd.html')
    cplist = company.objects.filter(id=id2)
    return render(request,'OJob/admin/CompanyUpdate.html',{'list':cplist})
def AddCompany(request):
    cname = request.POST.get("cname")
    tel = request.POST.get("phone")
    addrs = request.POST.get("address")
    id = request.POST.get("id")
    if not user.objects.filter(id=id).exists():
        return JsonResponse({"data": "error1"})
    if company.objects.filter(cname=cname).exists():
        return JsonResponse({"data":"error"})
    company.objects.create(cname=cname,cplace=addrs,ctel=tel,createid=id)
    object=user.objects.get(id=id)
    object.upower=2
    object.save()
    return JsonResponse({"data":"success"})
def UpdateCompany(request):
    cname = request.POST.get("cname")
    tel = request.POST.get("phone")
    addrs = request.POST.get("address")
    obj = company.objects.get(cname=cname)
    obj.ctel = tel
    obj.cplace = addrs
    obj.save()
    return JsonResponse({"tips": "修改成功"})
def DeleteCompany(request):
    id = request.POST.get("id")
    company.objects.filter(id=id).delete()
    return JsonResponse({"tips": "删除成功"})
def DeleteAllCompany(request):
    list1 = request.POST.getlist("list1[]")
    for i in list1:
        company.objects.filter(id=i).delete()
    return JsonResponse({"tips": "删除成功"})
def QueryCompany(request):
    upower = request.session.get('upower')
    cname = request.POST.get("cname")
    cplace = request.POST.get("place")
    if cname=="" and cplace=="":
        cplist=None
    elif cname=="":
        cplist=company.objects.filter(Q(cplace__contains=cplace))
    elif cplace=="":
        cplist = company.objects.filter(Q(cname__contains=cname))
    else:
        cplist=company.objects.filter(Q(cplace__contains=cplace) & Q(cname__contains=cname))
    return render(request,'OJob/admin/CompanyManage.html',{"cplist":cplist,"upower":upower,"id":1})

#留言信息管理
def ManageLeaveMge(request,id):
    upower = request.session.get('upower')
    lmlist = leavemge.objects.all()
    paginator = Paginator(lmlist, 4)
    id = int(id)
    if id < 1:
        id = 1
    try:
        lmlist = paginator.page(id)
    except EmptyPage:
        id = paginator.num_pages
        lmlist = paginator.page(paginator.num_pages)
    return render(request, 'OJob/admin/LeaveMgeManage.html', {"lmlist": lmlist, "upower": upower, "id": id})
def LeaveMgeOperation(request,id1,id2):
    id1=int(id1)
    if id1==0:
       return render(request,'OJob/admin/LeaveMgeAdd.html')
    lmlist = leavemge.objects.filter(id=id2)
    return render(request,'OJob/admin/LeaveMgeUpdate.html',{'list':lmlist})
def AddLeaveMge(request):
    cname = request.POST.get("cname")
    title = request.POST.get("title")
    content= request.POST.get("content")
    if user.objects.filter(uname=cname).exists():
         leavemge.objects.create(uname=cname, title=title, content=content, date=datetime.datetime.now())
         return JsonResponse({"data": "success"})
    return JsonResponse({"data": "error"})
def UpdateLeaveMge(request):
    id = request.POST.get("id")
    cname = request.POST.get("cname")
    title = request.POST.get("title")
    content = request.POST.get("content")
    obj = leavemge.objects.get(id=id)
    obj.title=title
    obj.content=content
    obj.save()
    return JsonResponse({"data":"success"})
def DeleteLeaveMge(request):
    id = request.POST.get("id")
    leavemge.objects.filter(id=id).delete()
    return JsonResponse({"tips": "删除成功"})
def DeleteAllLeaveMge(request):
    list1 = request.POST.getlist("list1[]")
    for i in list1:
        leavemge.objects.filter(id=i).delete()
    return JsonResponse({"tips": "删除成功"})
def QueryLeaveMge(request):
    upower = request.session.get('upower')
    cname = request.POST.get("cname")
    title = request.POST.get("title")
    print("***********")
    if cname=="" and title=="":
        lmlist=None
    elif cname=="":
        lmlist=leavemge.objects.filter(Q(title__contains=title))
    elif title=="":
        lmlist = leavemge.objects.filter(Q(uname__contains=cname))
    else:
        lmlist=leavemge.objects.filter(Q(title__contains=title) & Q(uname__contains=cname))
    return render(request,'OJob/admin/LeaveMgeManage.html',{"lmlist":lmlist,"upower":upower,"id":1})

#地点信息管理
def ManagePlace(request,id):
    upower = request.session.get('upower')
    lmlist = wkaddrs.objects.all()
    paginator = Paginator(lmlist, 4)
    id = int(id)
    if id < 1:
        id = 1
    try:
        lmlist = paginator.page(id)
    except EmptyPage:
        id = paginator.num_pages
        lmlist = paginator.page(paginator.num_pages)
    return render(request, 'OJob/admin/PlaceManage.html', {"list": lmlist, "upower": upower, "id": id})
def PlaceOperation(request,id1,id2):
    lmlist = wkaddrs.objects.filter(id=id2)
    return render(request,'OJob/admin/PlaceUpdate.html',{'list':lmlist})
def UpdatePlace(request):
    id = request.POST.get("id")
    addrs = request.POST.get("addrs")
    count = request.POST.get("count")
    obj = wkaddrs.objects.get(id=id)
    obj.addrs=addrs
    obj.count=count
    obj.save()
    return JsonResponse({"data":"success"})
def DeletePlace(request):
    id = request.POST.get("id")
    wkaddrs.objects.filter(id=id).delete()
    return JsonResponse({"tips": "删除成功"})
#权限管理
def ManageGrant(request,id):
    upower = request.session.get('upower')
    userlist = user.objects.filter(upower=1)
    paginator = Paginator(userlist, 4)
    id = int(id)
    if id < 1:
        id = 1
    try:
        list = paginator.page(id)
    except EmptyPage:
        id = paginator.num_pages
        list = paginator.page(paginator.num_pages)
    return render(request, 'OJob/admin/GrantManage.html', {"upower": upower, "userlist": list, "id": id})
def BindAdmin(request):
    id=request.POST.get("id")
    object=user.objects.get(id=id)
    object.upower=0
    object.save()
    return JsonResponse({"data":"success"})
def AddGrant(request,id):
    return render(request, 'OJob/admin/GrantAdd.html', {"id": id})
def BindCompany(request):
    id = request.POST.get("id")
    cname=request.POST.get("company")
    if company.objects.filter(cname=cname).exists():
        object=company.objects.get(cname=cname)
        object.createid=id
        object.save()
        object1=user.objects.get(id=id)
        object1.upower=2
        object1.save()
        return JsonResponse({"data":"success"})
    return JsonResponse({"data":"error"})
#审核招聘信息
def ManageAudit(request,id):
    upower = request.session.get('upower')
    lmlist = jobmge.objects.all()
    paginator = Paginator(lmlist, 4)
    id = int(id)
    if id < 1:
        id = 1
    try:
        lmlist = paginator.page(id)
    except EmptyPage:
        id = paginator.num_pages
        lmlist = paginator.page(paginator.num_pages)
    return render(request, 'OJob/admin/AuditRecruitInfo.html', {"upower": upower, "lmlist": lmlist, "id": id})
def AuditRecruitInfo(request):
    id=request.POST.get("id")
    isenter=request.POST.get("judge")
    object=jobmge.objects.get(id=id)
    object.isenter=isenter
    object.save()
    return JsonResponse({"data":"success"})