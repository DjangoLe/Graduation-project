from django.conf.urls import url
from . import views as views
from .admin import views as v
from .company import views as cv
from .user import views as uv
from django.contrib import admin
urlpatterns=[
   #用户界面
   url(r'^index/',views.index),
   url(r'^main/(\d+)/$', views.main),
   url(r'^login/(\d+)/$', views.login),
   url(r'^queryjob/$', views.queryjob),
   url(r'^queryposition/(\d+)/(.*)/$', views.queryposition),
   url(r'^leavemessage/$', views.leavemessage),
   url(r'^perfect_leavemge/$', views.perfect_leavemge),
   url(r'^leamge/(.*)/(\d+)/$', views.leamge),
   url(r'^register/$', views.register),
   url(r'^perfect_register/$', views.perfect_register),

   url(r'^backstage/$', views.backstage),
   #注册公司
   url(r'^cpyregister/$', views.cpyregister),
   url(r'^per_cpyregister/$', views.per_cpyregister),
   #报名参加
   url(r'^jobdetail/(\d+)/$', views.jobdetail),
   url(r'^JoinJob/$', views.JoinJob),
   #退出
   url(r'^quit/$', views.quit),

  ##############################################################

   #管理员界面

   #个人信息管理
   url(r'^MyManage/$', v.MyManage),
   url(r'^AddUser/$',v.AddUser),
   url(r'UpdatePasswd/(\d+)/$',v.UpdatePasswd),
   url(r'UpdateUserPasswd',v.UpdateUserPasswd),
   #用户信息管理
   url(r'^Manage_user/(\d+)/$',v.Manage_user),
   url(r'^UserOperation/(\d+)/(\d+)/$',v.UserOperation),
   url(r'^UpdateUser/$',v.UpdateUser),
   url(r'^DeleteUser/$',v.DeleteUser),
   url(r'^QueryUser/$',v.QueryUser),

   url(r'^DeleteAllUser/$', v.DeleteAllUser),
   #企业信息管理
   url(r'^ManageCompany/(\d+)/$',v.ManageCompany),
   url(r'^CompanyOperation/(\d+)/(\d+)/$',v.CompanyOperation),
   url(r'^AddCompany/$',v.AddCompany),
   url(r'^UpdateCompany/$',v.UpdateCompany),
   url(r'^DeleteCompany/$',v.DeleteCompany),
   url(r'^DeleteAllCompany/$', v.DeleteAllCompany),
   url(r'^QueryCompany/$',v.QueryCompany),
   #留言信息管理
   url(r'^ManageLeaveMge/(\d+)/$',v.ManageLeaveMge),
   url(r'^LeaveMgeOperation/(\d+)/(\d+)/$', v.LeaveMgeOperation),
   url(r'^AddLeaveMge/$', v.AddLeaveMge),
   url(r'^UpdateLeaveMge/$',v.UpdateLeaveMge),
   url(r'^DeleteLeaveMge/$',v.DeleteLeaveMge),
   url(r'^DeleteAllLeaveMge/$', v.DeleteAllLeaveMge),
   url(r'^QueryLeaveMge/$',v.QueryLeaveMge),
   #地点信息管理
   url(r'^ManagePlace/(\d+)/$', v.ManagePlace),
   url(r'^PlaceOperation/(\d+)/(\d+)/$', v.PlaceOperation),
   url(r'^UpdatePlace/$', v.UpdatePlace),
   url(r'^DeletePlace/$',v.DeletePlace),
   #用户权限管理
   url(r'^ManageGrant/(\d+)/$',v.ManageGrant),
   url(r'^BindAdmin/$',v.BindAdmin),
   url(r'^AddGrant/(\d+)/$',v.AddGrant),
   url(r'^BindCompany/$',v.BindCompany),
   #审核招聘信息
   url(r'^ManageAudit/(\d+)/$', v.ManageAudit),
   url(r'^AuditRecruitInfo/$', v.AuditRecruitInfo),

   ##############################################################

   #公司界面
   #公司信息管理
   url(r'^ManageComInfo/$',cv.ManageComInfo),
   #企业招聘信息管理
   url(r'^ManageRecruitInfo/(\d+)/$',cv.ManageRecruitInfo),
   url(r'^RecruitInfoOperation/(\d+)/(\d+)/$', cv.RecruitInfoOperation),
   url(r'^AddRecruitInfo/$', cv.AddRecruitInfo),
   url(r'^UpdateRecruitInfo/$',cv.UpdateRecruitInfo),
   url(r'^DeleteRecruitInfo/$',cv.DeleteRecruitInfo),
   url(r'^DeleteAllRecruitInfo/$', cv.DeleteAllRecruitInfo),
   url(r'^QueryRecruitInfo/$',cv.QueryRecruitInfo),
   #申请人审核
   url(r'^ManageAudit1/(\d+)/$',cv.ManageAudit),
   url(r'^AuditOperation/(\d+)/(\d+)/$', cv.AuditOperation),
   url(r'^HandleAudit/$',cv.HandleAudit),
   url(r'^AddAudit/$',cv.AddAudit),
   url(r'^DeleteAllAudit/$', cv.DeleteAllAudit),
   url(r'^QueryAudit/$',cv.QueryAudit),

   ##############################################################

   #用户后台界面

   #用户简历信息管理
   url(r'^ManageResume/$',uv.ManageResume),
   url(r'^ResumeOperation/(\d+)/(\d+)/$', uv.ResumeOperation),
   url(r'^AddResume/$', uv.AddResume),
   url(r'^UpdateResume/$', uv.UpdateResume),

   #投递情况管理
   url(r'^ManageDeliver/(\d+)/$', uv.ManageDeliver),
   url(r'^DeliverOperation/(\d+)/(\d+)/$', uv.DeliverOperation),
   url(r'^AddDeliver/$', uv.AddDeliver),
   url(r'^DeleteDeliver/$', uv.DeleteDeliver),
   url(r'^DeleteAllDeliver/$', uv.DeleteAllDeliver),
   url(r'^QueryDeliver/$', uv.QueryDeliver),

   #职位薪资分布
   url(r'^PlaceDistribute/$', uv.PlaceDistribute),
   url(r'^PositionDistribute/$', uv.PositionDistribute),


]