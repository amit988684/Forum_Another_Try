from django.db import models
from student.models import Course,Depart
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Assignment(models.Model):
    assignment_name = models.CharField(max_length=20)
    assignment_file = models.FileField(upload_to='teacher_assignment')
    share = models.BooleanField(default=False)
    deadline = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.assignment_name


class Slide(models.Model):
    slide_name = models.CharField(max_length=20)
    slide_file = models.FileField(upload_to='teacher_slide')
    share = models.BooleanField(default=False)

    def __str__(self):
        return self.slide_name


class DocumentTeacher(models.Model):
    document_name = models.CharField(max_length=20)
    document_file = models.FileField(upload_to='teacher_doc',blank=True)

    def __str__(self):
        return self.document_name

    def __unicode__(self):
        return self.document_name


class TeacherModel(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    default_name = 'teacher'
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30,blank=True)

    depart = models.ForeignKey(Depart)
    course = models.ForeignKey(Course,blank=True,null=True)

    contact = models.CharField(max_length=20,null=True,blank=True)
    email = models.EmailField(max_length=50,blank=True)
    resume = models.FileField(upload_to='teacher_resume', blank=True,null=True)
    profile_pic = models.FileField(upload_to='teacher_profile_pic', blank=True)
    # documents
    docs = models.ManyToManyField(DocumentTeacher,blank=True)
    assignment = models.ManyToManyField(Assignment,blank=True)
    slide = models.ManyToManyField(Slide,blank=True)
    # links
    github = models.URLField(max_length=100,null=True,blank=True)
    linkedin = models.URLField(max_length=100,null=True,blank=True)
    twitter = models.URLField(max_length=100,null=True,blank=True)
    works_links = models.CharField(max_length=200,blank=True)

    # def image_thumbnail(self):
    #     return '<img src="%s"/>' % self.profile_pic

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

