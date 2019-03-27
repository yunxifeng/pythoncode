from django.shortcuts import render
from django.http import HttpResponse

from django.core.urlresolvers import reverse
# Create your views here.
'''
views函数需要一个HttpResponse类型的参数
'''
def do_normalmap(request):
    return HttpResponse("This is normalmap.")
def withparam(request,year,month):
    return HttpResponse("This is the param {0},{1}".format(year,month))
def liudana(request):
    return HttpResponse("这是一个子路由")
def do_book(request,page_number):
    return HttpResponse("This page number is {0}".format(page_number))
def extremParam(request,name):
    return HttpResponse("my name is {0}".format(name))
def revParse(request):
    return HttpResponse("Your requested URL is {0}".format(reverse('askname')))