from django.shortcuts import render,redirect

import time,re
# Create your views here.
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password,check_password
def global_params(request):
    addresslist=[]
    hylist=[]
    jmlist=jobmge.objects.filter(isenter=1)
    addrslist=wkaddrs.objects.all()
    num1=len(addrslist)
    num2=0
    for i in range(0,num1):
        for j in range(0,num1):
            if addrslist[i].count>=addrslist[j].count:
                num2=num2+1
                if num1-num2<5:
                  addresslist.append(addrslist[i].addrs)
                  break
        if len(addresslist)>4:
            break
        num2=0
    for item in jmlist:
        if not item.jposition in hylist and not len(hylist)>3:
            hylist.append(item.jposition)
        # if not item.jplace in addresslist and not len(addresslist)>4:
        #     addresslist.append(item.jplace)
    lmlist=leavemge.objects.all()[0:6]
    jmlist = jobmge.objects.filter(isenter=1)[0:4]
    username = request.session.get('username', "游客")
    return {
        'addlist':addresslist,
        'hylist':hylist,
        'jmlist':jmlist,
        'lmlist':lmlist,
        "tips": "请输入内容",
        'username':username
    }
from django.core.paginator import Paginator, EmptyPage
def index(request):
    jmlist1=jobmge.objects.filter(isenter=1)[0:4]
    return render(request,'OJob/user/job.html',{'jmlist1':jmlist1,"id":1})
def main(request,id):
    jmlist1=jobmge.objects.filter(isenter=1)
    paginator = Paginator(jmlist1, 4)
    id = int(id)
    if id < 1:
        id = 1
    try:
        jmlist1 = paginator.page(id)
    except EmptyPage:
        id = paginator.num_pages
        jmlist1 = paginator.page(paginator.num_pages)
    return render(request,'OJob/user/job.html',{'jmlist1':jmlist1,"id":id})

#登陆

def login(request,id):
    tips=""
    if id=="1":
        return render(request,'OJob/user/login.html',{"data":tips})
    else:
        username=request.POST.get("username")
        passwd=request.POST.get("passwd")
        if user.objects.filter(uname=username,upasswd=passwd).exists():
            request.session["username"] = username
            return redirect("/main/1/")
        tips="(账号或者密码输入错误)"
        return render(request,'OJob/user/login.html',{"data":tips})

#用户公司注册
def register(request):
    return render(request,"OJob/user/register.html",{"data": ""})

def perfect_register(request):
    username = request.session.get("username")
    tips="注册成功"
    uname = request.POST.get("uname")
    judge=user.objects.filter(uname=uname).exists()
    if judge==True:
        tips="用户名已经存在"
        return render(request,"OJob/user/register.html",{"data": tips})
    if username==None or username=="游客":
        upasswd=request.POST.get("passwd")
        telephone=request.POST.get("tel")
        uaddress=request.POST.get("addrs")
        # upasswd=make_password(upasswd)
        user.objects.create(uname=uname,upasswd=upasswd,uaddress=uaddress,telephone=telephone)
        return redirect("/login/1/")
    tips = "您已经有账号"
    return render(request, "OJob/user/register.html", {"data": tips})


#模糊查询职位
def queryjob(request):

    flag=request.POST.get("name")
    content=request.POST.get("content")
    jmlist = jobmge.objects.filter(isenter=1)[0:4]
    if flag=="occup":
        jmlist1=jobmge.objects.filter(jposition__contains=content,isenter=1)[0:4]
    else:
        jmlist1 = jobmge.objects.filter(jplace__contains=content,isenter=1)[0:4]
    if jmlist1.count()==0:
        return render(request, 'OJob/user/job.html', {"jmlist1": jmlist, "tips": "输入有误,请重新输入","id":1})
    return render(request, 'OJob/user/job.html',{'jmlist1':jmlist1,"id":1})

#查询职位
def queryposition(request,judge1,judge2):
    if judge1=='1':
        qp=jobmge.objects.filter(jplace=judge2,isenter=1)[0:4]
    if judge1=='2':
        qp=jobmge.objects.filter(jposition=judge2,isenter=1)[0:4]
    return render(request,'OJob/user/job.html',{'jmlist1':qp,"id":1})

#填写留言信息
def leavemessage(request):
    username = request.session.get('username')
    data=""
    if username==None or username=="":
        data="请先登录"
        return render(request, 'OJob/user/leavemessage.html',{'username':username,"data":data})
    return render(request, 'OJob/user/leavemessage.html',{'username':username,"data":data})
import datetime
def perfect_leavemge(request):
    tips = "填写留言信息成功"
    uname = request.session.get('username')
    judge =user.objects.filter(uname=uname).exists()
    if judge==False:
        tips="用户名不存在"
        return render(request, 'OJob/user/leavemessage.html', {'username': uname, "data": tips})
    title = request.POST.get("subject")
    content= request.POST.get("mge")
    leavemge.objects.create(uname=uname,title=title,content=content,date=datetime.datetime.now())
    return render(request, 'OJob/user/leavemessage.html', {'username': uname, "data": tips})

def leamge(request,judge1,id):
    lmlist1=leavemge.objects.filter(title=judge1)[0:1]
    lmlist2 = leavemge.objects.all()
    paginator = Paginator(lmlist2, 4)
    id = int(id)
    if id < 1:
        id = 1
    try:
        lmlist2 = paginator.page(id)
    except EmptyPage:
        id = paginator.num_pages
        lmlist2 = paginator.page(paginator.num_pages)
    return render(request,"OJob/user/show_lmessage.html",{'lmlist1':lmlist1,"lmlist2":lmlist2,"id":id,"judge1":judge1})

def backstage(request):
    username = request.session.get('username')
    if username=="游客" or username==None:
      return render(request, 'OJob/user/login.html', {"data": ""})
    userlist = user.objects.filter(uname=username)[0:4]
    upower=""
    for item in userlist:
        upower=item.upower
    request.session["upower"]=upower

    return render(request,"OJob/admin/base.html",{"username":username,"list":userlist,"upower":upower})
#注册公司
def cpyregister(request):
    return render(request,"OJob/user/CompanyRegister.html",{"data":""})
def per_cpyregister(request):
    username = request.session.get('username')
    tips="注册成功"
    if username=="游客" or username==None:
        tips="请先登录"
        return render(request, "OJob/user/CompanyRegister.html",{"data": tips})
    userlist=user.objects.filter(uname=username)
    for item in userlist:
        id=item.id
    cplace = request.POST.get("addrs")
    cname = request.POST.get("uname")
    ctel = request.POST.get("tel")
    if company.objects.filter(cname=cname,createid=id).exists():
        tips="该公司已经存在"
        return render(request, "OJob/user/CompanyRegister.html", {"data": tips})
    if usernote.objects.filter(uname=username):
        usernote.objects.filter(uname=username).delete()
    object=user.objects.get(uname=username)
    object.upower=2
    object.save()
    company.objects.create(cname=cname,cplace=cplace,ctel=ctel,createid=id)

    return render(request, "OJob/user/CompanyRegister.html", {"data": tips})
#详情界面
def jobdetail(request,id):
    joblist=jobmge.objects.filter(id=id)
    for item in joblist:
        epname=item.epname
    cplist=company.objects.filter(cname=epname)
    return render(request, "OJob/user/JobDetail.html", {"cplist": cplist,"joblist":joblist})
#报名参加
def JoinJob(request):
    uname = request.session.get('username')
    if uname=="游客" or uname==None:
        return JsonResponse({"data": "error1"})
    if not usernote.objects.filter(uname=uname).exists():
        return JsonResponse({"data": "error2"})
    id=request.POST.get("id")
    jlist=jobmge.objects.filter(id=id)
    for item in jlist:
        epname=item.epname
        jposition=item.jposition
    print("***********")
    print(epname+jposition)
    if reply.objects.filter(uname=uname,jposition=jposition,epname=epname).exists():
        return JsonResponse({"data":"error"})
    reply.objects.create(uname=uname,epname=epname,jposition=jposition)
    return JsonResponse({"data": "success"})
#退出
def quit(request):
    request.session.flush()
    return redirect("/login/1/")