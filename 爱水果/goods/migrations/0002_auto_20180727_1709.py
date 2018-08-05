# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-27 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsinfo',
            options={},
        ),
        migrations.AlterModelOptions(
            name='typeinfo',
            options={},
        ),
        migrations.RemoveField(
            model_name='goodsinfo',
            name='gclick',
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='isjin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='isre',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='isxin',
            field=models.BooleanField(default=False),
        ),
    ]
