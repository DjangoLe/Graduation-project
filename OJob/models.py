from django.db import models

# Create your models here.
#用户信息表
class user(models.Model):
    uname=models.CharField(max_length=20,unique=True)
    upasswd=models.CharField(max_length=255)
    upower=models.IntegerField(default=1)

    uaddress=models.CharField(max_length=20,default='0')
    telephone=models.CharField(max_length=20,default='0')
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.uname
#简历信息表
class usernote(models.Model):
    uname = models.CharField(max_length=20, unique=True)
    realname=models.CharField(max_length=20)
    usex=models.CharField(max_length=20)
    uage=models.IntegerField(default=0)
    exp=models.CharField(max_length=100)
    telephone = models.CharField(max_length=20,default='0')
    language = models.CharField(max_length=20,default='0')
    #goalseat=models.CharField(max_length=50,default='0')
    edubg=models.CharField(max_length=50,default='0')
    #evaluation=models.CharField(max_length=100,default='0')

#留言表
class leavemge(models.Model):
    uname=models.CharField(max_length=20,default='0')
    title=models.CharField(max_length=20,default='0')
    content=models.CharField(max_length=20,default='0')
    date=models.DateTimeField()
    def __str__(self):
        return self.uname
#公司表
class company(models.Model):
    cname=models.CharField(max_length=20,default='0',unique=True)
    cplace=models.CharField(max_length=20,default='0')
    ctel=models.CharField(max_length=20,default='0')
    createid=models.IntegerField(default=0)
   # isallow=models.IntegerField(default=0)
    def __str__(self):
        return self.cname
#招聘信息表
class jobmge(models.Model):
    jposition=models.CharField(max_length=20)
    jplace=models.CharField(max_length=20,default='0')
    jwages=models.IntegerField(default=0)
    jcount=models.CharField(max_length=20,default='0')
    jskill=models.CharField(max_length=100,default='0')
    workexp=models.CharField(max_length=100,default='0')
    epid=models.IntegerField(default=0)
    epname=models.CharField(max_length=20,default='0')
    settime=models.DateTimeField()
    isenter=models.IntegerField(default=0)
    def __str__(self):
        return self.epname
#公司回应表
class reply(models.Model):
    uname=models.CharField(max_length=20,default='0')
    epname = models.CharField(max_length=20,default='0')
    jposition=models.CharField(max_length=20,default='0')
    substance=models.CharField(max_length=100,default='无')
    isenter=models.IntegerField(default=0)
    def __str__(self):
        return self.realname
#工作地点表
class wkaddrs(models.Model):
    addrs=models.CharField(max_length=50,default='0')
    count = models.IntegerField(default=0)
    isdel=models.CharField(max_length=50,default='0')
# #行业表
# class hangye(models.Model):
#     name=models.CharField(max_length=50)
#     status=models.CharField(max_length=50)