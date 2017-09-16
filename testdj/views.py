# -*- coding:utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from blogs.models import Blog
from login.models import User
from testdj import forms
from django.template import RequestContext


def login(request):
    if request.method == 'POST':
        uf = forms.UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #return render_to_response('success.html',{'username':username})
                blog_list = Blog.objects.all()
                return render_to_response('blog_list.html',{'username':username,'blog_list':blog_list})
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = forms.UserForm()
        print uf
    return render_to_response('login.html',{'uf':uf})

def blog_list(request):
    blog_list = Blog.objects.all()
    return render_to_response('blog_list.html',{'blog_list':blog_list})

def blog_form(request):
    if request.method == 'POST':
        print "----------------------sssss"
        if 'id' in request.POST:
            form = forms.EditForm(request.POST)
        else:
            form = forms.BlogForm(request.POST)
        print form
        print "----------------------end"
        if form.is_valid():
            print "----------------------end2"
            data = form.cleaned_data
            print data
            #form is contain the id , the if can delete
            if 'id' not in data: 
                print "----------------------ffffff"
                blog = Blog(title=data['title'],author=data['author'],content=data['content'])
                blog.save()
            else:
                print "----------------------test"
                print Blog.objects
                blog = Blog.objects.get(id=data['id'])
                blog.title = data['title']
                blog.author = data['author']
                blog.content = data['content']
                blog.save()
            return HttpResponseRedirect('/blog/list')    
    else:
        print request.method
        print "----------------------newsss"
        form = forms.BlogForm()
        print form
        #return render_to_response('blog_form.html',{'form':form},context_instance=RequestContext(request))
        return render_to_response('blog_form.html',{'form':form})

def blog_del(request):
    errors = []
    if 'id' in request.GET:
        bid_ = request.GET['id']
        Blog.objects.filter(id=bid_).delete()
        return HttpResponseRedirect('/blog/list')
    else:
        errors.append("参数异常请刷新后重试")
        return render_to_response('blog_list.html', {'errors': errors})

def blog_view(request):
    errors = []
    if 'id' in request.GET:
        bid_ = request.GET['id']
        blog = Blog.objects.get(id=bid_)
        #import markdown2
        #blog.content = markdown2.markdown(blog.content, extras=['fenced-code-blocks'], )
        #blog.content = markdown.markdown(blog.content,
        #                                  extensions=[
        #                                      'markdown.extensions.extra',
        #                                      'markdown.extensions.codehilite',
        #                                      'markdown.extensions.toc',
        #                                  ])
        return render_to_response('blog_view.html',{'blog':blog})
    else:
        errors.append("参数异常请刷新后重试")
        return render_to_response("blog_list.hmtl",{'errors':errors})


def blog_edit(request):
    errors = []
    if 'id' in request.GET:
        bid_ = request.GET['id']
        blog = Blog.objects.get(id=bid_)
        print blog
        #form = Blog.objects.filter(id=bid_).update(title=blog.title,author=blog.author,content=blog.content)
        form = forms.EditForm(
                initial = {'id':blog.id,'title':blog.title,'author':blog.author,'content':blog.content}        
        )
        #return render_to_response('blog_form.html',{'form':form},context_instance=RequestContext(request))
        return render_to_response('blog_form.html',{'form':form})
    else:
        errors.append("参数异常请刷新后重试")
        return render_to_response("blog_list.html",{'errors':errors})
