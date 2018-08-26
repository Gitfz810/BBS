from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64, help_text='标题')
    created = models.DateTimeField(auto_now_add=True, help_text='创建时间')
    content = models.TextField(help_text='内容')
