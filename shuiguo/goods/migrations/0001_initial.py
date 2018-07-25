# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-24 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=20, verbose_name='名字')),
                ('gpic', models.ImageField(upload_to='df_goods', verbose_name='图片')),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='价钱')),
                ('isDelete', models.BooleanField(default=False)),
                ('gunit', models.CharField(default='500g', max_length=20, verbose_name='单位')),
                ('gclick', models.IntegerField(verbose_name='点击')),
                ('gjianjie', models.CharField(max_length=200)),
                ('gkucun', models.IntegerField(verbose_name='库存')),
                ('gcontent', tinymce.models.HTMLField(verbose_name='描述')),
            ],
            options={
                'verbose_name_plural': '水果',
            },
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttitle', models.CharField(max_length=20, verbose_name='种类')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': '水果类型修改',
            },
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.TypeInfo'),
        ),
    ]
