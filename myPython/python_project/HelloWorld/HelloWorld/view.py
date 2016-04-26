#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'Hello World'
    context['cc'] = '这是内容'
    return render(request,'hello.html',context)
    #return HttpResponse('hello world')

def index(request):
     return render(request,'home.html')


