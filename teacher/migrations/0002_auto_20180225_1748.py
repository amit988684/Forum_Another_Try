# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-25 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentteacher',
            old_name='doc_file',
            new_name='document_file',
        ),
        migrations.RenameField(
            model_name='documentteacher',
            old_name='doc_name',
            new_name='document_name',
        ),
    ]
