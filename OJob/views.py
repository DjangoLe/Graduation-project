from django.shortcuts import render,redirect

import time,re
# Create your views here.
from django.http import HttpResponse
from OJob.models import user,wkaddrs,reply,hangye,jobmge,leavemge,usernote

def global_params(request):
    addresslist=wkaddrs.objects.all()
    hylist=hangye.objects.all()
    jmlist=jobmge.objects.all()
    lmlist=leavemge.objects.all()
    username = request.session.get('username', "游客")
    return {
        'addlist':addresslist,
        'hylist':hylist,
        'jmlist':jmlist,
        'lmlist':lmlist,
        "tips": "请输入内容",
        'username':username
    }
from  django.core.paginator import Paginator
def main(request):

    jmlist1=jobmge.objects.all()[0:4]
    return render(request,'OJob/user/job.html',{'jmlist1':jmlist1})

#登陆
def login(request,id):

    if id=="1":
        return render(request,'OJob/user/login.html')
    else:
       if request.method == "POST":
        username=request.POST.get("username")
        passwd=request.POST.get("passwd")
        try:
            flag1=user.objects.get(uname=username,upasswd=passwd)
        except:
            flag1=None
        finally:
            if flag1==None or flag1=="":
                return render(request,'OJob/user/login.html',{'sign':"账号、密码输入错误"})
            request.session["username"] = username

            return redirect("/main/")

#用户公司注册
def register(request):
    return render(request,"OJob/user/register.html")
from django.http import JsonResponse
def perfect_register(request):
    tips="恭喜你注册成功,请点击确定跳往主界面"
    uname = request.POST.get("uname")
    if uname=="":
        tips="用户名不能为空"
        return JsonResponse({"data": tips})
    judge=user.objects.filter(uname=uname).exists()
    if judge==True:
        tips="用户名已经存在"
        return JsonResponse({"data": tips})
    upasswd=request.POST.get("passwd")
    if upasswd=="":
        tips="密码不能为空"
        return JsonResponse({"data": tips})
    apply=request.POST.get("apply")
    telephone=request.POST.get("tel")
    uaddress=request.POST.get("addrs")
    if apply=="user":
        upower=1
    else:
        upower=2
    user.objects.create(uname=uname,upasswd=upasswd,upower=upower,uaddress=uaddress,telephone=telephone,ucount=0,isDelete=0)
    return JsonResponse({"data":tips})


#模糊查询职位
def queryjob(request):

    flag=request.POST.get("name")
    content=request.POST.get("content")
    jmlist = jobmge.objects.all()
    if flag=="occup":
        jmlist1=jobmge.objects.filter(jposition__contains=content)
    else:
        jmlist1 = jobmge.objects.filter(jplace__contains=content)
    if jmlist1.count()==0:
        return render(request, 'OJob/user/job.html', {"jmlist1": jmlist, "tips": "输入有误,请重新输入"})
    return render(request, 'OJob/user/job.html',{'jmlist1':jmlist1})

#查询职位
def queryposition(request,judge1,judge2):
    if judge1=='1':
        qp=jobmge.objects.filter(jplace=judge2)
    if judge1=='2':
        qp=jobmge.objects.filter(jposition=judge2)
    return render(request,'OJob/user/job.html',{'jmlist1':qp})
#简历填写
def resume(request):
    username = request.session.get('username')
    if username==None or username=="":
        pass
    return render(request, 'OJob/user/resume.html',{'username':username})

#保存简历信息到数据库
def perfect_resume(request):
    realname = request.POST.get("realname")
    tips="填写简历成功,请点击确定跳往主界面"
    if realname=="":
        tips="真实姓名不能为空"
        return JsonResponse({"data": tips})
    judge = usernote.objects.filter(realname=realname).exists()
    if judge==True:
        tips="你已经填写过简历信息"
        return JsonResponse({"data": tips})
    tel=request.POST.get("tel")
    if tel=="":
        tips="请输入正确的手机号"
        return JsonResponse({"data": tips})
    sex = request.POST.get("sex")
    age = request.POST.get("age")
    if re.match(r'^((1[0-5])|[1-9])?\d$',age)==None:
        tips="请输入正确的年龄"
        return JsonResponse({"data": tips})
    exp = request.POST.get("exp")
    language = request.POST.get("language")
    goalseat = request.POST.get("goalseat")
    edu = request.POST.get("edu")
    evalu= request.POST.get("evalu")
    if sex=="man":
        sex="男"
    sex="女"
    if exp=="no":
        exp="无经验"
    elif exp=="one":
        exp="一年"
    elif exp=="two":
        exp="两年"
    else:
        exp="两年以上"

    usernote.objects.create(realname=realname,usex=sex,uage=age,exp=exp,telephone=tel,language
                            =language,goalseat=goalseat,edubg=edu,evaluation=evalu)
    return JsonResponse({"data": tips})
#填写留言信息
def leavemessage(request):
    username = request.session.get('username')
    if username==None or username=="":
        pass
    return render(request, 'OJob/user/leavemessage.html',{'username':username})
import datetime
def perfect_leavemge(request):
    tips = "填写留言信息成功,请点击确定跳往主界面"
    uname = request.POST.get("name")
    judge =leavemge.objects.filter(uname=uname).exists()
    if judge==False:
        tips="用户名不存在"
        return JsonResponse({"data": tips})
    title = request.POST.get("subject")
    if title == "":
        tips = "标题不能为空"
        return JsonResponse({"data": tips})
    content= request.POST.get("mge")
    leavemge.objects.create(uname=uname,title=title,content=content,date=datetime.datetime.now())
    return JsonResponse({"data": tips})

def leamge(request,judge1):
    lmlist1=leavemge.objects.filter(title=judge1)
    lmlist = leavemge.objects.all()[0:4]
    return render(request,"OJob/user/show_lmessage.html",{'lmlist1':lmlist1,"lmlist":lmlist})

def backstage(request):
    return render(request,"OJob/admin/base.html")