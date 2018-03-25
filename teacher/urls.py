from django.conf.urls import url
from teacher import views

# app_name="teacher"
urlpatterns = [
    url(r'^teacher/(?P<username>[\w.@+-]+)/$', views.teacher_profile, name='teacher_profile'),


]
