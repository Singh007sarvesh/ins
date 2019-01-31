from django.urls import path
from . import views, userlist, user
from django.conf.urls import url

urlpatterns = [
  	path('user/', userlist.UserList.as_view(), name = 'user'),
  	url(r'^user/(?P<pk>[0-9]+)/$', user.User.as_view()),

]