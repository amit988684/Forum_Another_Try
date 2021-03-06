# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-27 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20180225_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='assignment',
            field=models.ManyToManyField(blank=True, to='teacher.Assignment'),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='docs',
            field=models.ManyToManyField(blank=True, to='teacher.DocumentTeacher'),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='teacher_resume'),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='slide',
            field=models.ManyToManyField(blank=True, to='teacher.Slide'),
        ),
    ]
