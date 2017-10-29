# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-25 19:44
from __future__ import unicode_literals
from django.db import migrations
from django.core.management import call_command


def loadfixture(apps, schema_editor):
    call_command('loaddata', 'initial_language.json')


class Migration(migrations.Migration):
    
    dependencies = [
        ('AutoGrade', '0014_auto_20171025_2316'),
    ]

    operations = [
        migrations.RunPython(loadfixture),
    ]