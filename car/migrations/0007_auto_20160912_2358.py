# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 23:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_car_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='accounts.MyProfile'),
        ),
    ]
