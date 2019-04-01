from django.db import models

# Create your models here.
#用户信息表
class user(models.Model):
    uname=models.CharField(max_length=20)
    upasswd=models.CharField(max_length=20)
    upower=models.IntegerField()

    uaddress=models.CharField(max_length=20)
    telephone=models.CharField(max_length=20)
    ucount=models.IntegerField()

    isDelete = models.BooleanField(default=False)
#简历信息表
class usernote(models.Model):
    realname=models.CharField(max_length=20)
    usex=models.CharField(max_length=20)
    uage=models.IntegerField()
    exp=models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    goalseat=models.CharField(max_length=50)
    edubg=models.CharField(max_length=50)
    evaluation=models.CharField(max_length=100)
    uuser=models.ForeignKey("user")
#留言表
class leavemge(models.Model):
    uname=models.CharField(max_length=20)
    title=models.CharField(max_length=20)
    content=models.CharField(max_length=20)
    date=models.DateTimeField()
    uuser = models.ForeignKey("user")
#公司表
class company(models.Model):
    cname=models.CharField(max_length=20)
    cplace=models.CharField(max_length=20)
    ctel=models.CharField(max_length=20)
#招聘信息表
class jobmge(models.Model):
    jposition=models.CharField(max_length=20)
    jplace=models.CharField(max_length=20)
    jwages=models.IntegerField()
    jcount=models.CharField(max_length=20)
    jskill=models.CharField(max_length=100)
    mgetype=models.CharField(max_length=20)
    epname=models.CharField(max_length=20)
    epcontent=models.CharField(max_length=100)
    boon=models.CharField(max_length=20)
    settime=models.DateTimeField()
    ccompany=models.ForeignKey("company")
#公司回应表
class reply(models.Model):
    realname=models.CharField(max_length=20)
    epname = models.CharField(max_length=20)
    substance=models.CharField(max_length=100)
    isenter=models.IntegerField()
    ccompany = models.ForeignKey("company")
    uuser = models.ForeignKey("user")
#工作地点表
class wkaddrs(models.Model):
    addrs=models.CharField(max_length=50)
    isdel=models.CharField(max_length=50)
#行业表
class hangye(models.Model):
    name=models.CharField(max_length=50)
    status=models.CharField(max_length=50)