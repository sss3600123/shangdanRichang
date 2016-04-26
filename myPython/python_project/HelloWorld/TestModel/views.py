#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(u"欢迎光临hh！！")

def test_ss(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def test_sss(request,a,b):
    c = int(a) + int(b)
    return  HttpResponse(str(c))

def mban(request):
    return render(request,'newhome.html')