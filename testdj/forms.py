#vim: set fileencoding=utf-8:
# -*- coding:utf-8 -*-

from django import forms

class BlogForm(forms.Form):
    #need deconde("gbk"), canot parse
    #id = forms.CharField(label='id',widget=forms.HiddenInput)
    #id = forms.CharField(label='id')
    title =  forms.CharField(label='����'.decode('GBK'))
    author = forms.CharField(label='����'.decode('GBK'))
    content = forms.CharField(label='����'.decode('GBk'),widget=forms.Textarea)

class EditForm(forms.Form):
    #need deconde("gbk"), canot parse
    id = forms.CharField(label='id',widget=forms.HiddenInput)
    #id = forms.CharField(label='id')
    title =  forms.CharField(label='����'.decode('GBK'))
    author = forms.CharField(label='����'.decode('GBK'))
    content = forms.CharField(label='����'.decode('GBk'),widget=forms.Textarea)

#�����¼��ģ��
class UserForm(forms.Form):
    username = forms.CharField(label='�û�����',max_length=100)
    password = forms.CharField(label='���룺',widget=forms.PasswordInput())
