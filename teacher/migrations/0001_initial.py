# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-25 04:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0002_auto_20180225_0434'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=20)),
                ('doc_file', models.FileField(blank=True, upload_to='teacher_doc')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('contact', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('resume', models.FileField(blank=True, upload_to='teacher_resume')),
                ('profile_pic', models.FileField(blank=True, upload_to='teacher_profile_pic')),
                ('github', models.URLField(blank=True, max_length=100, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=100, null=True)),
                ('twitter', models.URLField(blank=True, max_length=100, null=True)),
                ('works_links', models.CharField(blank=True, max_length=200)),
                ('course', models.ManyToManyField(to='student.Course')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Depart')),
                ('docs', models.ManyToManyField(to='teacher.DocumentTeacher')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
