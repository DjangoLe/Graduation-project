# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-05-12 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OJob', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='upasswd',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='wkaddrs',
            name='addrs',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='wkaddrs',
            name='isdel',
            field=models.CharField(default='0', max_length=50),
        ),
    ]