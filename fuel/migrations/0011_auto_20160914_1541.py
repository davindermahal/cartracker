# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160912_2358'),
        ('fuel', '0010_auto_20160914_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.MyProfile', to_field='user_id')),
            ],
        ),
        migrations.AddField(
            model_name='fillup',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fuel.Payment'),
        ),
    ]
