# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-05-12 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190512_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.IntegerField(choices=[(1, '注册'), (0, '找回密码'), (2, '修改邮箱')], verbose_name='验证码类型'),
        ),
    ]
