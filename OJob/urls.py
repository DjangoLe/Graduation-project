from django.conf.urls import url
from OJob import views as views
from OJob.admin import views as v
urlpatterns=[
   #用户界面
   url(r'^main/$', views.main),
   url(r'^login/(\d+)/$', views.login),
   url(r'^queryjob/$', views.queryjob),
   url(r'^queryposition/(\d+)/(.*)/$', views.queryposition),
   url(r'^resume/$', views.resume),
   url(r'^perfect_resume/$', views.perfect_resume),
   url(r'^leavemessage/$', views.leavemessage),
   url(r'^perfect_leavemge', views.perfect_leavemge),
   url(r'^leamge/(.*)/$', views.leamge),
   url(r'^register/$', views.register),
   url(r'^perfect_register/$', views.perfect_register),
   url(r'^backstage/$', views.backstage),
   #管理员界面
   url(r'^base/$', v.base),
   url(r'^user_mag/$',v.user_mag),
   url(r'^usernote_mag/$',v.usernote_mag),
]