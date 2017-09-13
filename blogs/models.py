#vim: set fileencoding=utf-8:
from django.db import models
# Create your models here.

class Blog(models.Model):
    title      = models.CharField('标题'.decode("GBK"), max_length=50)
    author     = models.CharField('作者'.decode("GBK"), max_length=10)
    content    = models.CharField('正文'.decode("GBK"), max_length=2000)
    post_date  = models.DateTimeField('发布时间'.decode("GBK"),auto_now_add=True)

    class Meta:
        ordering = ['-post_date']
