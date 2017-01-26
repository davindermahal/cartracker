# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160912_2358'),
        ('fuel', '0009_auto_20160914_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='accounts.MyProfile', to_field='user_id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='accounts.MyProfile', to_field='user_id'),
            preserve_default=False,
        ),
    ]
