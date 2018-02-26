from django.conf.urls import url
# from django.contrib import admin
from blogging import views

urlpatterns = [
    url(r'^$', views.user_login, name='user_login'),
]
