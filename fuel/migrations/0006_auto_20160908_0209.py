# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 02:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0005_auto_20160908_0205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fillup',
            old_name='car_id',
            new_name='car',
        ),
    ]
