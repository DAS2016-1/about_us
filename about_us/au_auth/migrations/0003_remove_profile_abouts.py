# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 17:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('au_auth', '0002_profile_abouts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='abouts',
        ),
    ]
