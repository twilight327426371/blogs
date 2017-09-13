#vim: set fileencoding=utf-8:
from django.db import models
# Create your models here.

class Blog(models.Model):
    title      = models.CharField('����'.decode("GBK"), max_length=50)
    author     = models.CharField('����'.decode("GBK"), max_length=10)
    content    = models.CharField('����'.decode("GBK"), max_length=2000)
    post_date  = models.DateTimeField('����ʱ��'.decode("GBK"),auto_now_add=True)

    class Meta:
        ordering = ['-post_date']
