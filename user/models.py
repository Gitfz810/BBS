from django.db import models


class User(models.Model):

    SEX = (
        ('M', '男'),
        ('F', '女'),
        ('U', '保密'),
    )

    nickname = models.CharField(max_length=64, unique=True, help_text='昵称')
    password = models.CharField(max_length=128, help_text='密码')
    icon = models.ImageField(help_text='头像')
    age = models.IntegerField(help_text='年龄')
    sex = models.CharField(max_length=8, choices=SEX, help_text='性别')
