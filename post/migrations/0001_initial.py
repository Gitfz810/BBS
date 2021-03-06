# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-26 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='标题', max_length=64)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('content', models.TextField(help_text='内容')),
            ],
        ),
    ]
