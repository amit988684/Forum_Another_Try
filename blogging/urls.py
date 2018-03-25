from django.conf.urls import url
from django.contrib.auth.views import login
from blogging import views
from teacher import views as teacher_view

app_name='blogging'

urlpatterns = [
    url(r'^$', views.user_login, name='user_login'),
    # url(r'^teacher/(?P<pk>\d+)/$',teacher_view, name="account-landing"),
    url(r'^admin/login/$',login, name='admin_login'),
]
