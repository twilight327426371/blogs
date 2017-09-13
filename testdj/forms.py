#vim: set fileencoding=utf-8:
# -*- coding:utf-8 -*-

from django import forms

class BlogForm(forms.Form):
    #need deconde("gbk"), canot parse
    #id = forms.CharField(label='id',widget=forms.HiddenInput)
    #id = forms.CharField(label='id')
    title =  forms.CharField(label='标题'.decode('GBK'))
    author = forms.CharField(label='作者'.decode('GBK'))
    content = forms.CharField(label='正文'.decode('GBk'),widget=forms.Textarea)

class EditForm(forms.Form):
    #need deconde("gbk"), canot parse
    id = forms.CharField(label='id',widget=forms.HiddenInput)
    #id = forms.CharField(label='id')
    title =  forms.CharField(label='标题'.decode('GBK'))
    author = forms.CharField(label='作者'.decode('GBK'))
    content = forms.CharField(label='正文'.decode('GBk'),widget=forms.Textarea)

#定义登录表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())
