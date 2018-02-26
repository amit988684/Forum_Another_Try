from django.db import models
from django.contrib.auth.models import User
# from django.core import validators
# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.course_name.lower()

    def __unicode__(self):
        return self.course_name.lower()


class Depart(models.Model):
    depart_name = models.CharField(max_length=30)

    def __str__(self):
        return self.depart_name

    def __unicode__(self):
        return self.depart_name


class DocumentStudent(models.Model):
    doc_name = models.CharField(max_length=20)
    doc_file = models.FileField(upload_to='student_doc',blank=True)

    def __str__(self):
        return self.doc_name

    def __unicode__(self):
        return self.doc_name



class StudentModel(models.Model):
    user = models.OneToOneField(User)
    default_name='student'
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30,blank=True)

    depart = models.ForeignKey(Depart)
    course = models.ManyToManyField(Course)

    contact = models.CharField(max_length=20,null=True,blank=True)
    email = models.EmailField(max_length=50,blank=True)
    resume = models.FileField(upload_to='student_resume', blank=True)
    profile_pic = models.FileField(upload_to='student_profile_pic', blank=True)

    docs = models.ManyToManyField(DocumentStudent)

    # links
    github = models.URLField(max_length=100,null=True,blank=True)
    linkedin = models.URLField(max_length=100,null=True,blank=True)
    twitter = models.URLField(max_length=100,null=True,blank=True)
    works_links = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

